# Use an official PHP runtime as a base image
FROM php:7.4-apache

# Install the MySQLi extension
RUN docker-php-ext-install mysqli

# Set the working directory to /var/www/html
WORKDIR /var/www/html

# Copy the current directory contents into the container at /var/www/html
COPY . /var/www/html

# Expose port 80 for Apache
EXPOSE 80

# Start Apache when the container runs
CMD ["apache2-foreground"]
