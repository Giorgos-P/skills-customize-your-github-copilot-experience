# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build scalable and modern REST APIs using the FastAPI framework. You'll create a complete API that handles HTTP requests, manages data, and follows REST principles, gaining practical experience with web development fundamentals and API design.

## 📝 Tasks

### 🛠️ Set Up FastAPI and Create Basic Endpoints

#### Description
Initialize a FastAPI application and create basic GET and POST endpoints to understand how to handle HTTP requests and return JSON responses.

#### Requirements
Your API must:

- Install and configure FastAPI with Uvicorn server
- Create a GET endpoint that returns a list of items
- Create a POST endpoint that accepts JSON data and returns a success response
- Use proper HTTP status codes (200 for success, 201 for created)
- Include appropriate request/response models using Pydantic


### 🛠️ Implement CRUD Operations

#### Description
Build complete Create, Read, Update, and Delete operations for a resource (e.g., tasks, books, or students) with proper data validation and error handling.

#### Requirements
Your API must:

- Implement GET endpoint to retrieve all items or a specific item by ID
- Implement POST endpoint to create new items with validation
- Implement PUT endpoint to update existing items
- Implement DELETE endpoint to remove items
- Return appropriate error responses for invalid requests or missing items
- Store data in memory or use a simple database
