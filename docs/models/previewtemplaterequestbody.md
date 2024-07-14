# PreviewTemplateRequestBody

Required parameters


## Fields

| Field                                                                                                                                                                                      | Type                                                                                                                                                                                       | Required                                                                                                                                                                                   | Description                                                                                                                                                                                | Example                                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `subject`                                                                                                                                                                                  | *OptionalNullable[str]*                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                         | The email subject.<br/>Applicable only to email templates.                                                                                                                                 | Welcome to our service!                                                                                                                                                                    |
| `body`                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                         | The template body before variable interpolation                                                                                                                                            | Hi, thank you for joining our service.                                                                                                                                                     |
| `from_email_name`                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                         | The local part of the From email address that will be used for emails.<br/>For example, in the address 'hello@example.com', the local part is 'hello'.<br/>Applicable only to email templates. | hello                                                                                                                                                                                      |
| `reply_to_email_name`                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                         | The local part of the Reply To email address that will be used for emails.<br/>For example, in the address 'hello@example.com', the local part is 'hello'.<br/>Applicable only to email templates. | support                                                                                                                                                                                    |