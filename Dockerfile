#first stage
FROM python:3.11-slim AS Server_socket

# http://bugs.python.org/issue19846
# > В настоящий момент настройка "LANG=C" в Linux *полностью выводит из строя Python 3*, а это плохо.
ENV LANG C.UTF-8

WORKDIR /src
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY server.py /src
EXPOSE 5051
EXPOSE 5051/udp
EXPOSE 9990:9999/udp

ENTRYPOINT [ "python" ]
CMD ["./server.py"]