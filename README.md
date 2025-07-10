# FastAPI Greeting API – From Notebook to Cloud

This repository demonstrates how to implement a simple FastAPI-based greeting service, starting with a [Jupyter Notebook](https://jupyter.org/) and extending all the way to cloud deployment.

The project is designed to balance simplicity and practicality: It’s a hands-on, beginner-friendly walkthrough for learning how to build, test, and deploy a Python API, useful for hackathons, personal projects, or even as a starting point for more robust enterprise services.

## What’s Included

The core idea is a small FastAPI app that returns a personalized greeting using two API styles:

- GET request with query parameters (e.g. `?name=Alice`)
- POST request with a JSON payload (e.g. `{ "name": "Alice" }`)

You’ll find:

- A [Jupyter notebook](./notebooks/fast-api-greeting-server.ipynb) which implement the FastAPI app.
- Several [client notebooks](./notebooks/) for testing the API from Python (GET & POST variants).
- An [HTML frontend](./docs/) deployed on [GitHub Pages](https://chrwittm.github.io/fastapi-greeting-api/) for local testing (you need to start the server from the [server notebook](./notebooks/fast-api-greeting-server.ipynb)).
- Two deployment examples:

  - A free-tier, [educational cloud deployment using Render.com](./notebooks/fast-api-greeting-deployment-render.ipynb)
  - An [enterprise-grade deployment to SAP BTP (Cloud Foundry)](./notebooks/fast-api-greeting-deployment-btp.ipynb)

## How to Run the API Locally

You can run the API locally by cloning this repo and running the provided notebooks.

## Related Blog Posts

The following blog posts explain each step in detail.

- [Implementing a Greeting API with FastAPI](https://chrwittm.github.io/posts/2025-07-08-implementing-fastapi-greeting/): Develop a simple API using FastAPI in a Jupyter Notebook.
- [Deploying a FastAPI App to the Cloud](https://chrwittm.github.io/posts/2025-07-09-deploying-fastapi-app-on-render/): Shows how to package the API for deployment and run it on [Render](https://render.com/). (Educational setup, free-tier)
- [Deploying a FastAPI App to SAP BTP](https://chrwittm.github.io/posts/2025-07-10-deploying-fastapi-app-on-sap-btp/): Take the same API and deploy it to SAP BTP (Cloud Foundry). (Enterprise-style deployment)