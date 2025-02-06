#Dockerfile for nginx 1.19
FROM nginx:1.19
RUN groupadd -S nginx && useradd -S nginx -G nginx && \
    chown -R nginx:nginx /var/chache && \
    chown -R nginx:nginx /var/log/nginx && \
    chown -R nginx:nginx /var/run && \
    chmod 755 /etc/nginx
COPY nginx.conf /etc/nginx
EXPOSE 80
USER nginx
CMD ["nginx" "deamonoff"]
