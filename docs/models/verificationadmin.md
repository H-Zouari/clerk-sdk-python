# VerificationAdmin


## Fields

| Field                                                                                        | Type                                                                                         | Required                                                                                     | Description                                                                                  | Example                                                                                      |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `status`                                                                                     | [models.AdminVerificationPhoneNumberStatus](../models/adminverificationphonenumberstatus.md) | :heavy_check_mark:                                                                           | N/A                                                                                          | verified                                                                                     |
| `strategy`                                                                                   | [models.AdminVerificationStrategy](../models/adminverificationstrategy.md)                   | :heavy_check_mark:                                                                           | N/A                                                                                          | admin                                                                                        |
| `attempts`                                                                                   | *OptionalNullable[int]*                                                                      | :heavy_minus_sign:                                                                           | N/A                                                                                          | 0                                                                                            |
| `expire_at`                                                                                  | *OptionalNullable[int]*                                                                      | :heavy_minus_sign:                                                                           | N/A                                                                                          | 1620000000                                                                                   |