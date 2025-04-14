# Video to MP3 Converter

A microservices-based system that allows users to upload videos, convert them to MP3s, and receive a download link via email. Each component is deployed as a Kubernetes service in a cluster.

## Workflow Overview

1. **Video Upload**
   - User uploads a video via the **API Gateway**.
   - Gateway:
     - Authenticates user using **JWT** (validated against user data in **MySQL**).
     - Stores the video in **MongoDB**.
     - Publishes a message to **RabbitMQ** for processing.

2. **Conversion Service**
   - Subscribes to RabbitMQ for new video upload messages.
   - Retrieves the video from MongoDB.
   - Converts it to MP3.
   - Stores the MP3 file back in MongoDB.
   - Publishes a new message indicating the job is complete.

3. **Notification Service**
   - Consumes messages about completed conversions.
   - Queries **MySQL** to fetch user email.
   - Sends an email with a download link.

4. **MP3 Download**
   - User requests the MP3 using:
     - A unique download ID.
     - Their JWT token.
   - API Gateway authenticates the request and streams the MP3 from MongoDB.

---

### Technologies Used

- Python
- Flask
- MongoDB
- MySQL
- RabbitMQ
- Docker
- Kubernetes

---

