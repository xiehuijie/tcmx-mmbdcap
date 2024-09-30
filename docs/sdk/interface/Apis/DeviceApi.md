# DeviceApi

All URIs are relative to *https://api.klab.ltd*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDevice**](DeviceApi.md#getDevice) | **GET** /device/{device_id} | 获取设备信息 |
| [**registerDevice**](DeviceApi.md#registerDevice) | **PUT** /device/register | 注册设备 |


<a name="getDevice"></a>
# **getDevice**
> GetDeviceSuccessResponse getDevice(device\_id)

获取设备信息

    获取设备信息

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **device\_id** | **String**|  | [default to null] |

### Return type

[**GetDeviceSuccessResponse**](../Models/GetDeviceSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="registerDevice"></a>
# **registerDevice**
> RegisterDeviceSuccessResponse registerDevice(RegisterDeviceBody)

注册设备

    在&#x60;Windows&#x60;平台下，使用&#x60;PowerShell&#x60;的&#x60;Get-CimInstance&#x60;命令去获取各类设备信息  如：使用&#x60;Get-CimInstance Win32_BIOS | ConvertTo-Json&#x60;获取BIOS信息

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **RegisterDeviceBody** | [**RegisterDeviceBody**](../Models/RegisterDeviceBody.md)|  | |

### Return type

[**RegisterDeviceSuccessResponse**](../Models/RegisterDeviceSuccessResponse.md)

### Authorization

[SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

