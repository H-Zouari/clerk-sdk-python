# Passkey


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    | Example                                                                        |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `status`                                                                       | [models.PasskeyVerificationStatus](../models/passkeyverificationstatus.md)     | :heavy_check_mark:                                                             | N/A                                                                            | verified                                                                       |
| `strategy`                                                                     | [models.PasskeyVerificationStrategy](../models/passkeyverificationstrategy.md) | :heavy_check_mark:                                                             | N/A                                                                            | passkey                                                                        |
| `nonce`                                                                        | [Optional[models.VerificationNonce]](../models/verificationnonce.md)           | :heavy_minus_sign:                                                             | N/A                                                                            | nonce_value                                                                    |
| `attempts`                                                                     | *OptionalNullable[int]*                                                        | :heavy_minus_sign:                                                             | N/A                                                                            | <nil>                                                                          |
| `expire_at`                                                                    | *OptionalNullable[int]*                                                        | :heavy_minus_sign:                                                             | N/A                                                                            | <nil>                                                                          |