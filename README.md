# Assignment1_AWS_DS

# UniEvent – Scalable University Event Management System on AWS

## Project Overview

UniEvent is a cloud-hosted web application designed for universities to manage and publish official events. The platform allows students to browse events, register for activities, and upload event-related media such as posters or images. The system automatically fetches event data from an external Open API and displays it as official university events.

This project demonstrates a **secure, scalable, and fault-tolerant AWS architecture** using core AWS services.

---

## Objectives

* Design a scalable cloud architecture on AWS
* Deploy a web application on EC2 instances
* Use Elastic Load Balancer for high availability
* Store event images securely in S3
* Automatically fetch event data from an external Open API
* Implement secure access using IAM
* Ensure fault tolerance if an EC2 instance fails

---

## External Open API

For this project, an external events API such as the following can be used:

* Ticketmaster API
* Eventbrite API
* RapidAPI Public Events API

The API must provide event data in JSON format including:

* Event Title
* Event Date
* Event Venue
* Event Description
* Event Image (optional)

The application periodically fetches event data using scheduled scripts running on EC2.

---

## AWS Architecture Design

### 1. VPC (Virtual Private Cloud)

The system is deployed inside a custom VPC for security and network isolation.

**VPC Components**

* Public Subnet

  * Elastic Load Balancer
  * NAT Gateway
* Private Subnet

  * EC2 Instances (Web Application Servers)
* Internet Gateway for external access

This ensures EC2 instances are not directly accessible from the internet.

---

### 2. EC2 (Elastic Compute Cloud)

* Multiple EC2 instances are deployed in **private subnets**
* Hosts the UniEvent web application
* Runs scripts to fetch event data from external API
* Auto Scaling can be enabled for handling peak loads

---

### 3. Elastic Load Balancer (ELB)

* Distributes traffic across multiple EC2 instances
* Ensures high availability and fault tolerance
* If one EC2 instance fails, traffic is routed to healthy instances

---

### 4. S3 (Simple Storage Service)

Used for:

* Storing event posters/images
* Storing fetched event JSON data (optional)
* Backup storage

**Security:**

* Buckets are private
* Access controlled using IAM roles
* Only EC2 instances can upload/read images

---

### 5. IAM (Identity and Access Management)

IAM is used to implement least-privilege access.

**IAM Roles**

* EC2 Role:

  * Read/Write access to S3 bucket
  * Permission to fetch data from external API
* Admin Role:

  * Full access to AWS resources
* User Role:

  * Limited access for monitoring

---

## System Workflow

1. User opens UniEvent website.
2. Request goes to Elastic Load Balancer.
3. ELB forwards request to one of the EC2 instances.
4. EC2 application fetches event data from external Open API.
5. Event data is processed and stored.
6. Event images are stored in S3.
7. Website displays events to users.
8. If one EC2 instance fails, ELB routes traffic to another instance.

---

## Architecture Diagram (Text Representation)

```
                Internet
                    |
            Internet Gateway
                    |
              Elastic Load Balancer
                    |
           -----------------------
           |                     |
      EC2 Instance 1       EC2 Instance 2
        (Private Subnet)    (Private Subnet)
           |                     |
           ----------------------
                       |
                      S3 Bucket
               (Images + Event Data)
                       |
                External Events API
```

---

## Security Best Practices Implemented

* EC2 instances in private subnet
* S3 bucket is private
* IAM roles with least privilege
* Security Groups restrict traffic
* Load balancer handles public traffic only
* NAT Gateway used for EC2 to access external API securely

---

## Scalability & Fault Tolerance

* Elastic Load Balancer distributes traffic
* Multiple EC2 instances ensure high availability
* Auto Scaling handles peak registration periods
* S3 provides highly durable storage

---

## Technologies Used

* AWS EC2
* AWS S3
* AWS IAM
* AWS VPC
* AWS Elastic Load Balancer
* External Events API
* Linux
* Python / Node.js (for API fetching script)
* HTML/CSS/JavaScript (Frontend)

---

## How to Deploy (Step-by-Step Summary)

1. Create VPC with public and private subnets
2. Create Internet Gateway and NAT Gateway
3. Launch EC2 instances in private subnet
4. Create S3 bucket for event images
5. Create IAM role and attach to EC2
6. Install web app on EC2
7. Configure Load Balancer
8. Configure Auto Scaling (optional)
9. Integrate External Events API
10. Test fault tolerance by stopping one EC2 instance

---

## Expected Outcome

* Students can view university events online
* Events automatically fetched from external API
* Images stored securely in S3
* System remains available during high traffic
* System continues working even if one server fails

---


Cloud Architecture Project – UniEvent System
University Cloud Computing Assignment

