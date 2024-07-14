# CreateSAMLConnectionRequestBody


## Fields

| Field                                                                                                                | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          | Example                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `name`                                                                                                               | *str*                                                                                                                | :heavy_check_mark:                                                                                                   | The name to use as a label for this SAML Connection                                                                  | My SAML Connection                                                                                                   |
| `domain`                                                                                                             | *str*                                                                                                                | :heavy_check_mark:                                                                                                   | The domain of your organization. Sign in flows using an email with this domain, will use this SAML Connection.       | example.org                                                                                                          |
| `provider`                                                                                                           | [models.Provider](../models/provider.md)                                                                             | :heavy_check_mark:                                                                                                   | The IdP provider of the connection.                                                                                  | saml_custom                                                                                                          |
| `idp_entity_id`                                                                                                      | *OptionalNullable[str]*                                                                                              | :heavy_minus_sign:                                                                                                   | The Entity ID as provided by the IdP                                                                                 | http://idp.example.org/                                                                                              |
| `idp_sso_url`                                                                                                        | *OptionalNullable[str]*                                                                                              | :heavy_minus_sign:                                                                                                   | The Single-Sign On URL as provided by the IdP                                                                        | http://idp.example.org/sso                                                                                           |
| `idp_certificate`                                                                                                    | *OptionalNullable[str]*                                                                                              | :heavy_minus_sign:                                                                                                   | The X.509 certificate as provided by the IdP                                                                         | MIIDdzCCAl+gAwIBAgIJAKcyBaiiz+DT...                                                                                  |
| `idp_metadata_url`                                                                                                   | *OptionalNullable[str]*                                                                                              | :heavy_minus_sign:                                                                                                   | The URL which serves the IdP metadata. If present, it takes priority over the corresponding individual properties    | http://idp.example.org/metadata.xml                                                                                  |
| `idp_metadata`                                                                                                       | *OptionalNullable[str]*                                                                                              | :heavy_minus_sign:                                                                                                   | The XML content of the IdP metadata file. If present, it takes priority over the corresponding individual properties | <EntityDescriptor ...                                                                                                |
| `attribute_mapping`                                                                                                  | [OptionalNullable[models.CreateSAMLConnectionAttributeMapping]](../models/createsamlconnectionattributemapping.md)   | :heavy_minus_sign:                                                                                                   | Define the attribute name mapping between Identity Provider and Clerk's user properties                              |                                                                                                                      |