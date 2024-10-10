# Exercise - A

URL: http://127.0.0.1:5601/app/dev_tools#/console

## Query 1

```
POST /salary-survey-index-202410/_search
{
  "size": 0,
  "query": {
    "match": {
      "job_details.title": "engineer"
    }
  },
  "aggs": {
    "average_salary": {
      "avg": {
        "field": "salary_details.annual_salary"
      }
    }
  }
}

```

<details>
<summary>Response</summary>

```json
{
  "took": 9,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 3994,
      "relation": "eq"
    },
    "max_score": null,
    "hits": []
  },
  "aggregations": {
    "average_salary": {
      "value": 237629.1136711503
    }
  }
}
```

</details>

## Query 2

```
POST /salary-survey-index-202410/_search
{
  "size": 0,
  "aggs": {
    "group_by_cities": {
      "terms": {
        "field": "employment_details.location_country",
        "size": 10
      },
      "aggs": {
        "average_salary": {
          "avg": {
            "field": "salary_details.annual_salary"
          }
        },
        "min_salary": {
          "min": {
            "field": "salary_details.annual_salary"
          }
        },
        "max_salary": {
          "max": {
            "field": "salary_details.annual_salary"
          }
        }
      }
    }
  }
}

```

<details>
<summary>Response</summary>

```json
{
  "took": 28,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 10000,
      "relation": "gte"
    },
    "max_score": null,
    "hits": []
  },
  "aggregations": {
    "group_by_cities": {
      "doc_count_error_upper_bound": 0,
      "sum_other_doc_count": 432,
      "buckets": [
        {
          "key": "United States (US)",
          "doc_count": 2972,
          "max_salary": {
            "value": null
          },
          "min_salary": {
            "value": null
          },
          "average_salary": {
            "value": null
          }
        },
        {
          "key": "Canada (CA)",
          "doc_count": 253,
          "max_salary": {
            "value": null
          },
          "min_salary": {
            "value": null
          },
          "average_salary": {
            "value": null
          }
        },
        {
          "key": "United Kingdom (GB)",
          "doc_count": 239,
          "max_salary": {
            "value": null
          },
          "min_salary": {
            "value": null
          },
          "average_salary": {
            "value": null
          }
        },
        {
          "key": "Australia (AU)",
          "doc_count": 186,
          "max_salary": {
            "value": null
          },
          "min_salary": {
            "value": null
          },
          "average_salary": {
            "value": null
          }
        },
        {
          "key": "Germany (DE)",
          "doc_count": 119,
          "max_salary": {
            "value": null
          },
          "min_salary": {
            "value": null
          },
          "average_salary": {
            "value": null
          }
        },
        {
          "key": "Netherlands (NL)",
          "doc_count": 51,
          "max_salary": {
            "value": null
          },
          "min_salary": {
            "value": null
          },
          "average_salary": {
            "value": null
          }
        },
        {
          "key": "France (FR)",
          "doc_count": 42,
          "max_salary": {
            "value": null
          },
          "min_salary": {
            "value": null
          },
          "average_salary": {
            "value": null
          }
        },
        {
          "key": "Sweden (SE)",
          "doc_count": 40,
          "max_salary": {
            "value": null
          },
          "min_salary": {
            "value": null
          },
          "average_salary": {
            "value": null
          }
        },
        {
          "key": "New Zealand (NZ)",
          "doc_count": 35,
          "max_salary": {
            "value": null
          },
          "min_salary": {
            "value": null
          },
          "average_salary": {
            "value": null
          }
        },
        {
          "key": "Switzerland (CH)",
          "doc_count": 35,
          "max_salary": {
            "value": null
          },
          "min_salary": {
            "value": null
          },
          "average_salary": {
            "value": null
          }
        }
      ]
    }
  }
}
```

</details>
