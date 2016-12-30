FROM jfloff/alpine-python:latest-slim

# Copy harambot files in
COPY /run.py /run.py
COPY /googcal.py /googcal.py
COPY /attendance.py /attendance.py

# Copy the credentials files
COPY .credentials /root/.credentials

# Add all of the python packages we need.
RUN pip install discord.py \
  && pip install asyncio \
  && pip install --upgrade google-api-python-client \
	&& pip install httplib2 \
	&& pip install texttable

# Define the command.
CMD ["python", "/run.py", "-d"]
