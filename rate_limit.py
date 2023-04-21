from flask import request, jsonify
import datetime

request_count = {}


def limit_requests(func):
    def wrapper(*args, **kwargs):

        client_ip = request.remote_addr

        if client_ip in request_count:
            if request_count[client_ip]['requests'] >= 50:

                return jsonify({'error': 'Request limit exceeded. Please try again later.'}), 429

            else:
                request_count[client_ip]['requests'] += 1
        else:
            request_count[client_ip] = {'requests': 1, 'start_time': datetime.datetime.now()}

        elapsed_time = (datetime.datetime.now() - request_count[client_ip]['start_time']).seconds / 3600.0

        if elapsed_time >= 1:
            request_count[client_ip]['requests'] = 1

            request_count[client_ip]['start_time'] = datetime.datetime.now()

        return func(*args, **kwargs)

    return wrapper
