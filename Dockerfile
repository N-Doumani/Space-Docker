# Use the official Nginx image as the base
FROM nginx:latest

# Optional: Copy your custom website files into Nginx's default public directory
COPY ./html /usr/share/nginx/html

# Expose port 80 to allow web traffic
EXPOSE 80

# Start Nginx in the foreground (default behavior of the base image)
CMD ["nginx", "-g", "daemon off;"]