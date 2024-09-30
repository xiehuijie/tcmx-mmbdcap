# CommonApi

All URIs are relative to *https://api.klab.ltd*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getErrorMap**](CommonApi.md#getErrorMap) | **GET** /common/errorMap | 获取错误码映射表 |
| [**getNotice**](CommonApi.md#getNotice) | **GET** /common/notice | 获取通知 |
| [**getStatus**](CommonApi.md#getStatus) | **GET** /common/status | 获取服务器状态 |
| [**login**](CommonApi.md#login) | **POST** /common/login | 登录 |
| [**register**](CommonApi.md#register) | **POST** /common/signUp | 注册 |
| [**setSystemNotice**](CommonApi.md#setSystemNotice) | **POST** /common/notice | 设置系统级公告 |
| [**weChatLogin**](CommonApi.md#weChatLogin) | **PATCH** /common/wechatLogin | 微信登录 |


<a name="getErrorMap"></a>
# **getErrorMap**
> GetErrorMapSuccessResponse getErrorMap()

获取错误码映射表

    获取错误码与错误信息的映射表

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetErrorMapSuccessResponse**](../Models/GetErrorMapSuccessResponse.md)

### Authorization

[SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getNotice"></a>
# **getNotice**
> GetNoticeSuccessResponse getNotice()

获取通知

    获取通知公告，将返回一个列表，包含当前应当显示的所有公告，可能有系统级公告、单位级公告等

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetNoticeSuccessResponse**](../Models/GetNoticeSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getStatus"></a>
# **getStatus**
> GetStatusSuccessResponse getStatus()

获取服务器状态

    获取服务器运行状态及信息

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetStatusSuccessResponse**](../Models/GetStatusSuccessResponse.md)

### Authorization

[SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="login"></a>
# **login**
> LoginSuccessResponse login(LoginBody)

登录

    &#x60;password&#x60;需在客户端对原始密码进行哈希，标准算法为&#x60;sha1(sha1(PASSWORD) + PASSWORD)，因此此处限制为40字符&#x60;  &#x60;device_id&#x60;需要通过[&#x60;获取设备ID&#x60;](/dr?m&#x3D;device&amp;i&#x3D;RegisterDevice)接口获取

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **LoginBody** | [**LoginBody**](../Models/LoginBody.md)|  | |

### Return type

[**LoginSuccessResponse**](../Models/LoginSuccessResponse.md)

### Authorization

[SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="register"></a>
# **register**
> RegisterSuccessResponse register(RegisterBody)

注册

    在平台内进行注册，在注册时需填入一个授权码，表明即将注册的用户属于哪个单位，该注册码由单位管理员生成

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **RegisterBody** | [**RegisterBody**](../Models/RegisterBody.md)|  | |

### Return type

[**RegisterSuccessResponse**](../Models/RegisterSuccessResponse.md)

### Authorization

[SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="setSystemNotice"></a>
# **setSystemNotice**
> SetSystemNoticeSuccessResponse setSystemNotice()

设置系统级公告

    设置系统级公告

### Parameters
This endpoint does not need any parameter.

### Return type

[**SetSystemNoticeSuccessResponse**](../Models/SetSystemNoticeSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="weChatLogin"></a>
# **weChatLogin**
> WeChatLoginSuccessResponse weChatLogin(WeChatLoginBody)

微信登录

    微信登录，需先请求[&#x60;获取二维码&#x60;](/dr?m&#x3D;wechat&amp;i&#x3D;GenerateWechatQrcode)接口后，再依据返回的&#x60;scan_id&#x60;请求此接口进行登录  &#x60;device_id&#x60;需要通过[&#x60;获取设备ID&#x60;](/dr?m&#x3D;device&amp;i&#x3D;RegisterDevice)接口获取

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **WeChatLoginBody** | [**WeChatLoginBody**](../Models/WeChatLoginBody.md)|  | |

### Return type

[**WeChatLoginSuccessResponse**](../Models/WeChatLoginSuccessResponse.md)

### Authorization

[SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

