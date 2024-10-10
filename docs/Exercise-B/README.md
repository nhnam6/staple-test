# Exercise - B

## GraphQL API Documentation

Before interacting with the GraphQL API, ensure you have the following setup on your local machine:

- A web browser or a GraphQL client tool such as [GraphQL Playground](https://github.com/graphql/graphql-playground) or [Postman](https://www.postman.com/).
- Network access to `http://127.0.0.1:5001/graphql`.

### Accessing the GraphQL API

The GraphQL API is accessible through the following URL: http://127.0.0.1:5001/graphql

### Example Queries

1. Get list records

```graphql
{
  listCompensation(salaryGte: 1, salaryLte: 10000, sortBy: "-timestamp") {
    id
    timestamp
    employmentDetails {
      employmentType
      companyName
      locationCountry
      locationCity
      industry
      publicPrivate
    }
  }
}
```

<details>
<summary>Example response</summary>

```json
{
  "data": {
    "listCompensation": [
      {
        "id": "HeULcpIBhAsA5iJvwIF_",
        "timestamp": 1608726074,
        "employmentDetails": {
          "employmentType": null,
          "companyName": null,
          "locationCountry": null,
          "locationCity": null,
          "industry": "Healthcare",
          "publicPrivate": null
        }
      },
      {
        "id": "2uULcpIBhAsA5iJvwIB_",
        "timestamp": 1602046504,
        "employmentDetails": {
          "employmentType": null,
          "companyName": null,
          "locationCountry": null,
          "locationCity": null,
          "industry": "sports footwear",
          "publicPrivate": null
        }
      },
      {
        "id": "3-ULcpIBhAsA5iJvwH9-",
        "timestamp": 1589463444,
        "employmentDetails": {
          "employmentType": null,
          "companyName": null,
          "locationCountry": null,
          "locationCity": null,
          "industry": "Education",
          "publicPrivate": null
        }
      },
      {
        "id": "r-ULcpIBhAsA5iJvwH9-",
        "timestamp": 1584510871,
        "employmentDetails": {
          "employmentType": null,
          "companyName": null,
          "locationCountry": null,
          "locationCity": null,
          "industry": "Public Relations",
          "publicPrivate": null
        }
      },
      {
        "id": "j-ULcpIBhAsA5iJvwH9O",
        "timestamp": 1583391198,
        "employmentDetails": {
          "employmentType": null,
          "companyName": null,
          "locationCountry": null,
          "locationCity": null,
          "industry": "ADVERTISING ",
          "publicPrivate": null
        }
      },
      {
        "id": "y-ULcpIBhAsA5iJvwH5O",
        "timestamp": 1580895190,
        "employmentDetails": {
          "employmentType": null,
          "companyName": null,
          "locationCountry": null,
          "locationCity": null,
          "industry": "Mortgage industry ",
          "publicPrivate": null
        }
      },
      {
        "id": "teULcpIBhAsA5iJvwH5O",
        "timestamp": 1580722657,
        "employmentDetails": {
          "employmentType": null,
          "companyName": null,
          "locationCountry": null,
          "locationCity": null,
          "industry": "advertising",
          "publicPrivate": null
        }
      },
      {
        "id": "peULcpIBhAsA5iJvwH0n",
        "timestamp": 1579016785,
        "employmentDetails": {
          "employmentType": null,
          "companyName": null,
          "locationCountry": null,
          "locationCity": null,
          "industry": "ARCHITECTURE",
          "publicPrivate": null
        }
      },
      {
        "id": "VeULcpIBhAsA5iJvwH0n",
        "timestamp": 1578412207,
        "employmentDetails": {
          "employmentType": null,
          "companyName": null,
          "locationCountry": null,
          "locationCity": null,
          "industry": "PR",
          "publicPrivate": null
        }
      },
      {
        "id": "UuULcpIBhAsA5iJvwH0n",
        "timestamp": 1578402322,
        "employmentDetails": {
          "employmentType": null,
          "companyName": null,
          "locationCountry": null,
          "locationCity": null,
          "industry": "",
          "publicPrivate": null
        }
      }
    ]
  }
}
```

</details>

2. Fetch a single record

```graphql
query {
  fetchCompensation(id: "teULcpIBhAsA5iJvwH5O") {
    id
    timestamp
  }
}
```

<details>
<summary>Example response</summary>

```json
{
  "data": {
    "fetchCompensation": {
      "id": "teULcpIBhAsA5iJvwH5O",
      "timestamp": 1580722657
    }
  }
}
```

</details>
