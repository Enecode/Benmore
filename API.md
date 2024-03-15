# API Documentation
## Introduction
This document outlines the API endpoints for managing projects and tasks.

Base URL: `http://127.0.0.1:8000/`

## Endpoints

### 1. Create Project
- **URL:** `/project-create/`
- **Method:** POST
- **Description:** Creates a new project.
- **Request Body:** JSON object containing project details.
    - `name` (string): The name of the project.
    - `description` (string, optional): Description of the project.
- **Response:** JSON object with the created project details.

### 2. Get All Projects
- **URL:** `/projects/`
- **Method:** GET
- **Description:** Retrieves a list of all projects.
- **Response:** JSON array containing details of all projects.

### 3. Get Project by ID
- **URL:** `/projects/<int:pk>/`
- **Method:** GET
- **Description:** Retrieves details of a specific project identified by its ID.
- **Path Parameters:**
    - `pk` (integer): The ID of the project.
- **Response:** JSON object containing details of the requested project.

### 4. Create Task
- **URL:** `/task-create/`
- **Method:** POST
- **Description:** Creates a new task associated with a project.
- **Request Body:** JSON object containing task details.
    - `name` (string): The name of the task.
    - `description` (string, optional): Description of the task.
    - `project_pk` (integer): The ID of the project the task belongs to.
- **Response:** JSON object with the created task details.

### 5. Get Tasks for a Project
- **URL:** `/projects/<int:project_pk>/tasks/`
- **Method:** GET
- **Description:** Retrieves a list of tasks associated with a specific project.
- **Path Parameters:**
    - `project_pk` (integer): The ID of the project.
- **Response:** JSON array containing details of all tasks associated with the project.

### 6. Get Task by ID
- **URL:** `/projects/<int:project_pk>/tasks/<int:pk>/`
- **Method:** GET
- **Description:** Retrieves details of a specific task associated with a project, identified by its ID.
- **Path Parameters:**
    - `project_pk` (integer): The ID of the project.
    - `pk` (integer): The ID of the task.
- **Response:** JSON object containing details of the requested task.

### 7. Filter Projects
- **URL:** `/filtered-projects/`
- **Method:** GET
- **Description:** Retrieves a filtered list of projects based on certain criteria.
- **Query Parameters:** (Optional)
    - `keyword` (string, optional): Filter projects by keyword.
    - `status` (string, optional): Filter projects by status.
- **Response:** JSON array containing details of filtered projects.

## Error Responses
- **400 Bad Request:** Invalid request format or missing parameters.
- **404 Not Found:** Resource not found.
- **500 Internal Server Error:** Server encountered an unexpected condition.

## Authentication and Authorization
- **Authentication:** API does not requires authentication.
- **Authorization:** The endpoints doe not require specific user roles or permissions for access.