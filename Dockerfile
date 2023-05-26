# Build Image
FROM    python:3.10-slim as builder
# Set the working directory to /jobs-website
WORKDIR /var/reluxx/
RUN apt-get update

RUN apt-get install -y binutils libproj-dev gdal-bin gpgv2 postgresql build-essential

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN pip install --upgrade pip

COPY  requirements.txt /tmp

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

FROM python:3.10-slim
# Run the image

EXPOSE  8000/tcp

RUN     mkdir -p /reluxx/ && \
        addgroup --gid 9999 python && \
        adduser --system --disabled-password --gecos '' --gid 9999 -uid 9999 python && \
        chown python:python /reluxx/

COPY    --from=builder /opt/venv /opt/venv

ENV     PYTHONPATH /reluxx/
ENV     PATH="/opt/venv/bin:$PATH"
COPY . .

CMD sh -c 'python manage.py migrate && python manage.py collectstatic --noinput && python manage.py runserver 0.0.0.0:8000'
