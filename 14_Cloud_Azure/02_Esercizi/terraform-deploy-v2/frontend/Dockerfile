FROM nginx:alpine

# Build argument for Function App URL
ARG FUNCTION_APP_URL=https://localhost:7071

# Remove default nginx html
RUN rm -rf /usr/share/nginx/html/*

# Copy static files and inject FUNCTION_APP_URL into index.html
COPY . /usr/share/nginx/html/
RUN sed -i "s|__FUNCTION_APP_URL__|\${FUNCTION_APP_URL}|g" /usr/share/nginx/html/index.html

# Expose port 80
EXPOSE 80

# Start nginx in foreground
CMD ["nginx", "-g", "daemon off;"]
