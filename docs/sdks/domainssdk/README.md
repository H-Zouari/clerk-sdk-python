# DomainsSDK
(*domains*)

### Available Operations

* [list](#list) - List all instance domains
* [add](#add) - Add a domain
* [delete](#delete) - Delete a satellite domain
* [update](#update) - Update a domain

## list

Use this endpoint to get a list of all domains for an instance.
The response will contain the primary domain for the instance and any satellite domains. Each domain in the response contains information about the URLs where Clerk operates and the required CNAME targets.

### Example Usage

```python
from clerk_backend_api import Clerk
import os

s = Clerk(
    bearer_auth=os.getenv("BEARER_AUTH", ""),
)


res = s.domains.list()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.Domains](../../models/domains.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## add

Add a new domain for your instance.
Useful in the case of multi-domain instances, allows adding satellite domains to an instance.
The new domain must have a `name`. The domain name can contain the port for development instances, like `localhost:3000`.
At the moment, instances can have only one primary domain, so the `is_satellite` parameter must be set to `true`.
If you're planning to configure the new satellite domain to run behind a proxy, pass the `proxy_url` parameter accordingly.

### Example Usage

```python
from clerk_backend_api import Clerk
import os

s = Clerk(
    bearer_auth=os.getenv("BEARER_AUTH", ""),
)


res = s.domains.add(name="example.com", is_satellite=True, proxy_url="https://proxy.example.com")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                 | Type                                                                                                                                      | Required                                                                                                                                  | Description                                                                                                                               | Example                                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `name`                                                                                                                                    | *str*                                                                                                                                     | :heavy_check_mark:                                                                                                                        | The new domain name. Can contain the port for development instances.                                                                      | example.com                                                                                                                               |
| `is_satellite`                                                                                                                            | *bool*                                                                                                                                    | :heavy_check_mark:                                                                                                                        | Marks the new domain as satellite. Only `true` is accepted at the moment.                                                                 | true                                                                                                                                      |
| `proxy_url`                                                                                                                               | *Optional[str]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | The full URL of the proxy which will forward requests to the Clerk Frontend API for this domain. Applicable only to production instances. | https://proxy.example.com                                                                                                                 |
| `retries`                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                          | :heavy_minus_sign:                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                       |                                                                                                                                           |


### Response

**[models.Domain](../../models/domain.md)**
### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400,402,422        | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |

## delete

Deletes a satellite domain for the instance.
It is currently not possible to delete the instance's primary domain.

### Example Usage

```python
from clerk_backend_api import Clerk
import os

s = Clerk(
    bearer_auth=os.getenv("BEARER_AUTH", ""),
)


res = s.domains.delete(domain_id="domain_12345")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            | Example                                                                |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `domain_id`                                                            | *str*                                                                  | :heavy_check_mark:                                                     | The ID of the domain that will be deleted. Must be a satellite domain. | domain_12345                                                           |
| `retries`                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)       | :heavy_minus_sign:                                                     | Configuration to override the default retry behavior of the client.    |                                                                        |


### Response

**[models.DeletedObject](../../models/deletedobject.md)**
### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 403,404            | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |

## update

The `proxy_url` can be updated only for production instances.
Update one of the instance's domains. Both primary and satellite domains can be updated.
If you choose to use Clerk via proxy, use this endpoint to specify the `proxy_url`.
Whenever you decide you'd rather switch to DNS setup for Clerk, simply set `proxy_url`
to `null` for the domain. When you update a production instance's primary domain name,
you have to make sure that you've completed all the necessary setup steps for DNS and
emails to work. Expect downtime otherwise. Updating a primary domain's name will also
update the instance's home origin, affecting the default application paths.

### Example Usage

```python
from clerk_backend_api import Clerk
import os

s = Clerk(
    bearer_auth=os.getenv("BEARER_AUTH", ""),
)


res = s.domains.update(domain_id="domain_12345", name="example.com", proxy_url="http://proxy.example.com")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                                      | Type                                                                                                                                                                                           | Required                                                                                                                                                                                       | Description                                                                                                                                                                                    | Example                                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `domain_id`                                                                                                                                                                                    | *str*                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                             | The ID of the domain that will be updated.                                                                                                                                                     | domain_12345                                                                                                                                                                                   |
| `name`                                                                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                             | The new domain name. For development instances, can contain the port,<br/>i.e `myhostname:3000`. For production instances, must be a valid FQDN,<br/>i.e `mysite.com`. Cannot contain protocol scheme. | example.com                                                                                                                                                                                    |
| `proxy_url`                                                                                                                                                                                    | *OptionalNullable[str]*                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                             | The full URL of the proxy that will forward requests to Clerk's Frontend API.<br/>Can only be updated for production instances.                                                                | http://proxy.example.com                                                                                                                                                                       |
| `retries`                                                                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                                                                            |                                                                                                                                                                                                |


### Response

**[models.Domain](../../models/domain.md)**
### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400,404,422        | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |