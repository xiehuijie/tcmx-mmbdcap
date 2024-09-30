# WechatApi

All URIs are relative to *https://api.klab.ltd*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**generateWechatQrcode**](WechatApi.md#generateWechatQrcode) | **GET** /wechat/qrcode | 微信二维码获取 |
| [**getWechatQrcodeResult**](WechatApi.md#getWechatQrcodeResult) | **GET** /wechat/qrcode/{scan_id} | Get Wechat Qrcode Result |
| [**weChatAuthorize**](WechatApi.md#weChatAuthorize) | **GET** /wechat/login | We Chat Authorize |
| [**wechatAccess**](WechatApi.md#wechatAccess) | **GET** /wechat | 微信接入验证 |
| [**wechatHandle**](WechatApi.md#wechatHandle) | **POST** /wechat | 微信消息处理 |


<a name="generateWechatQrcode"></a>
# **generateWechatQrcode**
> GenerateWechatQrcodeSuccessResponse generateWechatQrcode()

微信二维码获取

    微信二维码获取接口，请求后将会生成一个临时二维码，此处将返回与该二维码相关的信息，随后需使用对应&#x60;scan_id&#x60;去请求其他接口来获取扫描结果，或执行相关动作  如：[&#x60;直接获取结果&#x60;](/dr?m&#x3D;wechat&amp;i&#x3D;GetWechatQrcodeResult)、[&#x60;用户绑定微信&#x60;](/dr?m&#x3D;user&amp;i&#x3D;BindWechatConfirm)

### Parameters
This endpoint does not need any parameter.

### Return type

[**GenerateWechatQrcodeSuccessResponse**](../Models/GenerateWechatQrcodeSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getWechatQrcodeResult"></a>
# **getWechatQrcodeResult**
> GetWechatQrcodeResultSuccessResponse getWechatQrcodeResult(scan\_id)

Get Wechat Qrcode Result

    仅获取二维码的扫描结果，不执行任何动作

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **scan\_id** | **String**|  | [default to null] |

### Return type

[**GetWechatQrcodeResultSuccessResponse**](../Models/GetWechatQrcodeResultSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="weChatAuthorize"></a>
# **weChatAuthorize**
> weChatAuthorize(redirect\_uri)

We Chat Authorize

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **redirect\_uri** | **String**|  | [optional] [default to 123] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain, application/json

<a name="wechatAccess"></a>
# **wechatAccess**
> String wechatAccess(signature, timestamp, nonce, echostr)

微信接入验证

    微信接入验证接口，提供对微信接入请求的响应，参考[&#x60;微信官方接入指南&#x60;](https://developers.weixin.qq.com/doc/offiaccount/Basic_Information/Access_Overview.html)

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **signature** | **String**|  | [default to null] |
| **timestamp** | **String**|  | [default to null] |
| **nonce** | **String**|  | [default to null] |
| **echostr** | **String**|  | [default to null] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain

<a name="wechatHandle"></a>
# **wechatHandle**
> String wechatHandle()

微信消息处理

    微信消息处理接口，负责完成对微信消息的响应

### Parameters
This endpoint does not need any parameter.

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain

