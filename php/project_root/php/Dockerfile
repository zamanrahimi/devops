# Use the official PHP image with Apache
FROM php:8.2-apache

# Install MySQLi extension
RUN docker-php-ext-install mysqli

# Copy PHP application code to the container
COPY . /var/www/html

# Expose port 80 (this is optional as it is just a documentation, doesn't actually publish the port)
EXPOSE 80
