FROM python:3.9-slim 

WORKDIR /app 
COPY . /app  
RUN pip install --no-cache-dir -r requirements.txt 
EXPOSE 5000 8501 
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh  
CMD ["/entrypoint.sh"]