# UpdateSAMLConnectionRequestBody


## Fields

| Field                                                                                                                               | Type                                                                                                                                | Required                                                                                                                            | Description                                                                                                                         | Example                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `name`                                                                                                                              | *OptionalNullable[str]*                                                                                                             | :heavy_minus_sign:                                                                                                                  | The name of the new SAML Connection                                                                                                 | Example SAML Connection                                                                                                             |
| `domain`                                                                                                                            | *OptionalNullable[str]*                                                                                                             | :heavy_minus_sign:                                                                                                                  | The domain to use for the new SAML Connection                                                                                       | example.com                                                                                                                         |
| `idp_entity_id`                                                                                                                     | *OptionalNullable[str]*                                                                                                             | :heavy_minus_sign:                                                                                                                  | The entity id as provided by the IdP                                                                                                | entity_123                                                                                                                          |
| `idp_sso_url`                                                                                                                       | *OptionalNullable[str]*                                                                                                             | :heavy_minus_sign:                                                                                                                  | The SSO url as provided by the IdP                                                                                                  | https://idp.example.com/sso                                                                                                         |
| `idp_certificate`                                                                                                                   | *OptionalNullable[str]*                                                                                                             | :heavy_minus_sign:                                                                                                                  | The x509 certificated as provided by the IdP                                                                                        | MIIDBTCCAe2gAwIBAgIQ...                                                                                                             |
| `idp_metadata_url`                                                                                                                  | *OptionalNullable[str]*                                                                                                             | :heavy_minus_sign:                                                                                                                  | The URL which serves the IdP metadata. If present, it takes priority over the corresponding individual properties and replaces them | https://idp.example.com/metadata                                                                                                    |
| `idp_metadata`                                                                                                                      | *OptionalNullable[str]*                                                                                                             | :heavy_minus_sign:                                                                                                                  | The XML content of the IdP metadata file. If present, it takes priority over the corresponding individual properties                | <EntityDescriptor>...</EntityDescriptor>                                                                                            |
| `attribute_mapping`                                                                                                                 | [OptionalNullable[models.UpdateSAMLConnectionAttributeMapping]](../models/updatesamlconnectionattributemapping.md)                  | :heavy_minus_sign:                                                                                                                  | Define the atrtibute name mapping between Identity Provider and Clerk's user properties                                             |                                                                                                                                     |
| `active`                                                                                                                            | *OptionalNullable[bool]*                                                                                                            | :heavy_minus_sign:                                                                                                                  | Activate or de-activate the SAML Connection                                                                                         | true                                                                                                                                |
| `sync_user_attributes`                                                                                                              | *OptionalNullable[bool]*                                                                                                            | :heavy_minus_sign:                                                                                                                  | Controls whether to update the user's attributes in each sign-in                                                                    | false                                                                                                                               |
| `allow_subdomains`                                                                                                                  | *OptionalNullable[bool]*                                                                                                            | :heavy_minus_sign:                                                                                                                  | Allow users with an email address subdomain to use this connection in order to authenticate                                         | true                                                                                                                                |
| `allow_idp_initiated`                                                                                                               | *OptionalNullable[bool]*                                                                                                            | :heavy_minus_sign:                                                                                                                  | Enable or deactivate IdP-initiated flows                                                                                            | false                                                                                                                               |