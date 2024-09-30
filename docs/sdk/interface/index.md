# 接口文档

<a name="documentation-for-api-endpoints"></a>
## Documentation for API Endpoints

All URIs are relative to *https://api.klab.ltd*

| Class | Method | HTTP request | Description |
|------------ | ------------- | ------------- | -------------|
| *CommonApi* | [**getErrorMap**](Apis/CommonApi.md#geterrormap) | **GET** /common/errorMap | 获取错误码映射表 |
*CommonApi* | [**getNotice**](Apis/CommonApi.md#getnotice) | **GET** /common/notice | 获取通知 |
*CommonApi* | [**getStatus**](Apis/CommonApi.md#getstatus) | **GET** /common/status | 获取服务器状态 |
*CommonApi* | [**login**](Apis/CommonApi.md#login) | **POST** /common/login | 登录 |
*CommonApi* | [**register**](Apis/CommonApi.md#register) | **POST** /common/signUp | 注册 |
*CommonApi* | [**setSystemNotice**](Apis/CommonApi.md#setsystemnotice) | **POST** /common/notice | 设置系统级公告 |
*CommonApi* | [**weChatLogin**](Apis/CommonApi.md#wechatlogin) | **PATCH** /common/wechatLogin | 微信登录 |
| *DeviceApi* | [**getDevice**](Apis/DeviceApi.md#getdevice) | **GET** /device/{device_id} | 获取设备信息 |
*DeviceApi* | [**registerDevice**](Apis/DeviceApi.md#registerdevice) | **PUT** /device/register | 注册设备 |
| *EvaluationApi* | [**createEvaluation**](Apis/EvaluationApi.md#createevaluation) | **PUT** /evaluation | 创建评测项 |
*EvaluationApi* | [**createEvaluationRecord**](Apis/EvaluationApi.md#createevaluationrecord) | **PUT** /evaluation/record | 创建评测记录 |
*EvaluationApi* | [**createEvaluationRelease**](Apis/EvaluationApi.md#createevaluationrelease) | **PUT** /evaluation/{evaluation_id}/release | 创建评测项发布版本 |
*EvaluationApi* | [**deleteEvaluation**](Apis/EvaluationApi.md#deleteevaluation) | **DELETE** /evaluation/{evaluation_id} | 删除评测项 |
*EvaluationApi* | [**deleteEvaluationRecord**](Apis/EvaluationApi.md#deleteevaluationrecord) | **DELETE** /evaluation/record/{evaluation_record_id} | 删除评测记录 |
*EvaluationApi* | [**deleteEvaluationRelease**](Apis/EvaluationApi.md#deleteevaluationrelease) | **DELETE** /evaluation/release/{release_id} | 删除评测项发布版本 |
*EvaluationApi* | [**getEvaluationAnalyzer**](Apis/EvaluationApi.md#getevaluationanalyzer) | **GET** /evaluation/analyzer/{analyzer_id} | 获取评测记录分析器详情 |
*EvaluationApi* | [**getEvaluationAnalyzerList**](Apis/EvaluationApi.md#getevaluationanalyzerlist) | **GET** /evaluation/release/{release_id}/analyzer | 获取适用的分析器摘要列表 |
*EvaluationApi* | [**getEvaluationDetail**](Apis/EvaluationApi.md#getevaluationdetail) | **GET** /evaluation/{evaluation_id} | 获取评测项详情 |
*EvaluationApi* | [**getEvaluationList**](Apis/EvaluationApi.md#getevaluationlist) | **GET** /evaluation/list | 获取评测项列表 |
*EvaluationApi* | [**getEvaluationRecord**](Apis/EvaluationApi.md#getevaluationrecord) | **GET** /evaluation/record/{evaluation_record_id} | 获取评测记录 |
*EvaluationApi* | [**getEvaluationRecordBriefList**](Apis/EvaluationApi.md#getevaluationrecordbrieflist) | **GET** /evaluation/record/list | 获取评测记录列表 |
*EvaluationApi* | [**getEvaluationReleaseAnalyzerList**](Apis/EvaluationApi.md#getevaluationreleaseanalyzerlist) | **GET** /evaluation/release/{release_id}/python | 获取评测发布项Python文件 |
*EvaluationApi* | [**getEvaluationReleaseList**](Apis/EvaluationApi.md#getevaluationreleaselist) | **GET** /evaluation/{evaluation_id}/release/list | 获取评测项发布版本列表 |
*EvaluationApi* | [**getEvaluationReleaseProto**](Apis/EvaluationApi.md#getevaluationreleaseproto) | **GET** /evaluation/release/{release_id}/proto | 获取评测发布项Proto文件 |
*EvaluationApi* | [**searchEvaluationRecord**](Apis/EvaluationApi.md#searchevaluationrecord) | **POST** /evaluation/record/search | 搜索评测记录 |
*EvaluationApi* | [**updateEvaluation**](Apis/EvaluationApi.md#updateevaluation) | **PATCH** /evaluation/{evaluation_id} | 更新评测项 |
*EvaluationApi* | [**updateEvaluationRelease**](Apis/EvaluationApi.md#updateevaluationrelease) | **PATCH** /evaluation/release/{release_id} | 更新评测项发布版本 |
*EvaluationApi* | [**uploadEvaluationRecord**](Apis/EvaluationApi.md#uploadevaluationrecord) | **PATCH** /evaluation/record/{evaluation_record_id} | 更新评测记录 |
| *FileApi* | [**createUploadTask**](Apis/FileApi.md#createuploadtask) | **POST** /file/upload | 创建上传任务 |
*FileApi* | [**getFileDirectLink**](Apis/FileApi.md#getfiledirectlink) | **GET** /file/{file_id}/directLink | 获取文件直链 |
*FileApi* | [**getTusConfig**](Apis/FileApi.md#gettusconfig) | **OPTIONS** /file/upload | 获取Tus协议配置 |
*FileApi* | [**getUploadInfo**](Apis/FileApi.md#getuploadinfo) | **HEAD** /file/upload/{file_id} | 上传文件 |
*FileApi* | [**uploadFileChunk**](Apis/FileApi.md#uploadfilechunk) | **PATCH** /file/upload/{file_id} | 上传文件 |
*FileApi* | [**uploadFilePrecheck**](Apis/FileApi.md#uploadfileprecheck) | **POST** /file/upload/precheck | 文件上传预检 |
| *RootApi* | [**ping**](Apis/RootApi.md#ping) | **GET** /ping | 网络测试 |
*RootApi* | [**redirect**](Apis/RootApi.md#redirect) | **GET** /r/{target} | 重定向 |
*RootApi* | [**root**](Apis/RootApi.md#root) | **GET** / | 根路由 |
| *ScaleApi* | [**createScale**](Apis/ScaleApi.md#createscale) | **PUT** /scale | 创建量表 |
*ScaleApi* | [**getScaleDetail**](Apis/ScaleApi.md#getscaledetail) | **GET** /scale/{scale_id} | 获取量表信息 |
*ScaleApi* | [**getScaleList**](Apis/ScaleApi.md#getscalelist) | **GET** /scale/list | 获取量表列表 |
| *SubjectApi* | [**createSubject**](Apis/SubjectApi.md#createsubject) | **PUT** /subject | 创建受试者 |
*SubjectApi* | [**deleteSubject**](Apis/SubjectApi.md#deletesubject) | **DELETE** /subject/{subject_id} | 删除受试者 |
*SubjectApi* | [**getSubjectBriefList**](Apis/SubjectApi.md#getsubjectbrieflist) | **GET** /subject/list | 获取受试者摘要列表 |
*SubjectApi* | [**getSubjectDetail**](Apis/SubjectApi.md#getsubjectdetail) | **GET** /subject/{subject_id} | 获取受试者详情 |
*SubjectApi* | [**searchsubjectRecord**](Apis/SubjectApi.md#searchsubjectrecord) | **POST** /subject/search | 搜索受试者 |
*SubjectApi* | [**updateSubject**](Apis/SubjectApi.md#updatesubject) | **PATCH** /subject/{subject_id} | 更新受试者 |
| *UnitApi* | [**createRegistrationCode**](Apis/UnitApi.md#createregistrationcode) | **PUT** /unit/{unit_id}/registration_code | 生成注册码 |
*UnitApi* | [**createUnit**](Apis/UnitApi.md#createunit) | **PUT** /unit | 创建单位 |
*UnitApi* | [**deleteRegistrationCode**](Apis/UnitApi.md#deleteregistrationcode) | **DELETE** /unit/{unit_id}/registration_code/{code} | 删除注册码 |
*UnitApi* | [**deleteUnit**](Apis/UnitApi.md#deleteunit) | **DELETE** /unit/{unit_id} | 移除单位 |
*UnitApi* | [**getRegistrationCodeList**](Apis/UnitApi.md#getregistrationcodelist) | **GET** /unit/{unit_id}/registration_code/list | 获取注册码列表 |
*UnitApi* | [**getUnitConfig**](Apis/UnitApi.md#getunitconfig) | **GET** /unit/{unit_id}/config | 获取单位配置 |
*UnitApi* | [**getUnitDetail**](Apis/UnitApi.md#getunitdetail) | **GET** /unit/{unit_id} | 获取单位详细信息 |
*UnitApi* | [**getUnitDeviceList**](Apis/UnitApi.md#getunitdevicelist) | **GET** /unit/{unit_id}/device_list | 获取单位下设备摘要 |
*UnitApi* | [**getUnitList**](Apis/UnitApi.md#getunitlist) | **GET** /unit/list | 获取单位列表 |
*UnitApi* | [**getUnitUserList**](Apis/UnitApi.md#getunituserlist) | **GET** /unit/{unit_id}/user_list | 获取单位下用户摘要 |
*UnitApi* | [**updateUnitConfig**](Apis/UnitApi.md#updateunitconfig) | **PATCH** /unit/{unit_id}/config | 更新单位配置 |
*UnitApi* | [**updateUnitInfo**](Apis/UnitApi.md#updateunitinfo) | **PATCH** /unit/{unit_id} | 更新单位信息 |
| *UserApi* | [**bindWechatConfirm**](Apis/UserApi.md#bindwechatconfirm) | **PATCH** /user/self/wechat | 确认微信账号绑定结果 |
*UserApi* | [**createUser**](Apis/UserApi.md#createuser) | **PUT** /user | 创建用户 |
*UserApi* | [**deleteUser**](Apis/UserApi.md#deleteuser) | **DELETE** /user/{user_id} | 删除用户 |
*UserApi* | [**generateOTP**](Apis/UserApi.md#generateotp) | **POST** /user/self/otp | Generate Otp |
*UserApi* | [**getPermission**](Apis/UserApi.md#getpermission) | **GET** /user/{user_id}/permission | 获取其他用户的权限信息 |
*UserApi* | [**getSelfPermission**](Apis/UserApi.md#getselfpermission) | **GET** /user/self/permission | 获取自己的权限信息 |
*UserApi* | [**getSelfinfo**](Apis/UserApi.md#getselfinfo) | **GET** /user/self/userinfo | 获取自己的用户信息 |
*UserApi* | [**getUserConfig**](Apis/UserApi.md#getuserconfig) | **GET** /user/{user_id}/config | 获取用户配置 |
*UserApi* | [**getUserSource**](Apis/UserApi.md#getusersource) | **GET** /user/{user_id}/resource | 获取用户资源 |
*UserApi* | [**getUserinfo**](Apis/UserApi.md#getuserinfo) | **GET** /user/{user_id}/userinfo | 获取其他用户信息 |
*UserApi* | [**updatePermission**](Apis/UserApi.md#updatepermission) | **PATCH** /user/{user_id}/permission | 更新其他用户的权限 |
*UserApi* | [**updateSelfinfo**](Apis/UserApi.md#updateselfinfo) | **PATCH** /user/self/userinfo | 更新自己的用户信息 |
*UserApi* | [**updateUserConfig**](Apis/UserApi.md#updateuserconfig) | **PATCH** /user/{user_id}/config | 更新用户配置 |
*UserApi* | [**updateUserinfo**](Apis/UserApi.md#updateuserinfo) | **PATCH** /user/{user_id}/userinfo | 更新其他用户信息 |
| *WechatApi* | [**generateWechatQrcode**](Apis/WechatApi.md#generatewechatqrcode) | **GET** /wechat/qrcode | 微信二维码获取 |
*WechatApi* | [**getWechatQrcodeResult**](Apis/WechatApi.md#getwechatqrcoderesult) | **GET** /wechat/qrcode/{scan_id} | Get Wechat Qrcode Result |
*WechatApi* | [**weChatAuthorize**](Apis/WechatApi.md#wechatauthorize) | **GET** /wechat/login | We Chat Authorize |
*WechatApi* | [**wechatAccess**](Apis/WechatApi.md#wechataccess) | **GET** /wechat | 微信接入验证 |
*WechatApi* | [**wechatHandle**](Apis/WechatApi.md#wechathandle) | **POST** /wechat | 微信消息处理 |


<a name="documentation-for-models"></a>
## Documentation for Models

 - [BindWechatConfirmBody](./Models/BindWechatConfirmBody.md)
 - [BindWechatConfirmFailureResponse](./Models/BindWechatConfirmFailureResponse.md)
 - [BindWechatConfirmSuccessResponse](./Models/BindWechatConfirmSuccessResponse.md)
 - [CreateEvaluationBody](./Models/CreateEvaluationBody.md)
 - [CreateEvaluationFailureResponse](./Models/CreateEvaluationFailureResponse.md)
 - [CreateEvaluationRecordBody](./Models/CreateEvaluationRecordBody.md)
 - [CreateEvaluationRecordFailureResponse](./Models/CreateEvaluationRecordFailureResponse.md)
 - [CreateEvaluationRecordSuccessResponse](./Models/CreateEvaluationRecordSuccessResponse.md)
 - [CreateEvaluationReleaseBody](./Models/CreateEvaluationReleaseBody.md)
 - [CreateEvaluationReleaseFailureResponse](./Models/CreateEvaluationReleaseFailureResponse.md)
 - [CreateEvaluationReleaseSuccessResponse](./Models/CreateEvaluationReleaseSuccessResponse.md)
 - [CreateEvaluationSuccessResponse](./Models/CreateEvaluationSuccessResponse.md)
 - [CreateRegistrationCodeFailureResponse](./Models/CreateRegistrationCodeFailureResponse.md)
 - [CreateRegistrationCodeSuccessResponse](./Models/CreateRegistrationCodeSuccessResponse.md)
 - [CreateScaleFailureResponse](./Models/CreateScaleFailureResponse.md)
 - [CreateScaleSuccessResponse](./Models/CreateScaleSuccessResponse.md)
 - [CreateSubjectBody](./Models/CreateSubjectBody.md)
 - [CreateSubjectFailureResponse](./Models/CreateSubjectFailureResponse.md)
 - [CreateSubjectSuccessResponse](./Models/CreateSubjectSuccessResponse.md)
 - [CreateUnitBody](./Models/CreateUnitBody.md)
 - [CreateUnitFailureResponse](./Models/CreateUnitFailureResponse.md)
 - [CreateUnitSuccessResponse](./Models/CreateUnitSuccessResponse.md)
 - [CreateUploadTaskFailureResponse](./Models/CreateUploadTaskFailureResponse.md)
 - [CreateUserBody](./Models/CreateUserBody.md)
 - [CreateUserFailureResponse](./Models/CreateUserFailureResponse.md)
 - [CreateUserSuccessResponse](./Models/CreateUserSuccessResponse.md)
 - [DeleteEvaluationFailureResponse](./Models/DeleteEvaluationFailureResponse.md)
 - [DeleteEvaluationRecordFailureResponse](./Models/DeleteEvaluationRecordFailureResponse.md)
 - [DeleteEvaluationRecordSuccessResponse](./Models/DeleteEvaluationRecordSuccessResponse.md)
 - [DeleteEvaluationReleaseFailureResponse](./Models/DeleteEvaluationReleaseFailureResponse.md)
 - [DeleteEvaluationReleaseSuccessResponse](./Models/DeleteEvaluationReleaseSuccessResponse.md)
 - [DeleteEvaluationSuccessResponse](./Models/DeleteEvaluationSuccessResponse.md)
 - [DeleteRegistrationCodeFailureResponse](./Models/DeleteRegistrationCodeFailureResponse.md)
 - [DeleteRegistrationCodeSuccessResponse](./Models/DeleteRegistrationCodeSuccessResponse.md)
 - [DeleteSubjectFailureResponse](./Models/DeleteSubjectFailureResponse.md)
 - [DeleteSubjectSuccessResponse](./Models/DeleteSubjectSuccessResponse.md)
 - [DeleteUnitFailureResponse](./Models/DeleteUnitFailureResponse.md)
 - [DeleteUnitSuccessResponse](./Models/DeleteUnitSuccessResponse.md)
 - [DeleteUserFailureResponse](./Models/DeleteUserFailureResponse.md)
 - [DeleteUserSuccessResponse](./Models/DeleteUserSuccessResponse.md)
 - [DeviceBrief](./Models/DeviceBrief.md)
 - [DeviceInformation](./Models/DeviceInformation.md)
 - [ErrorDetails](./Models/ErrorDetails.md)
 - [ErrorDetails_loc_inner](./Models/ErrorDetails_loc_inner.md)
 - [EvaluationBrief](./Models/EvaluationBrief.md)
 - [EvaluationDetail](./Models/EvaluationDetail.md)
 - [EvaluationRecordAnalyzerBrief](./Models/EvaluationRecordAnalyzerBrief.md)
 - [EvaluationRecordAnalyzerDetail](./Models/EvaluationRecordAnalyzerDetail.md)
 - [EvaluationRecordAnalyzerIndicator](./Models/EvaluationRecordAnalyzerIndicator.md)
 - [EvaluationRecordAnalyzerIndicator_advice](./Models/EvaluationRecordAnalyzerIndicator_advice.md)
 - [EvaluationRecordBrief](./Models/EvaluationRecordBrief.md)
 - [EvaluationRecordDetail](./Models/EvaluationRecordDetail.md)
 - [EvaluationRecordScopeType](./Models/EvaluationRecordScopeType.md)
 - [EvaluationReleaseBrief](./Models/EvaluationReleaseBrief.md)
 - [EvaluationScopeType](./Models/EvaluationScopeType.md)
 - [GenerateOTPFailureResponse](./Models/GenerateOTPFailureResponse.md)
 - [GenerateOTPSuccessResponse](./Models/GenerateOTPSuccessResponse.md)
 - [GenerateWechatQrcodeFailureResponse](./Models/GenerateWechatQrcodeFailureResponse.md)
 - [GenerateWechatQrcodeReply](./Models/GenerateWechatQrcodeReply.md)
 - [GenerateWechatQrcodeSuccessResponse](./Models/GenerateWechatQrcodeSuccessResponse.md)
 - [GetDeviceFailureResponse](./Models/GetDeviceFailureResponse.md)
 - [GetDeviceSuccessResponse](./Models/GetDeviceSuccessResponse.md)
 - [GetErrorMapFailureResponse](./Models/GetErrorMapFailureResponse.md)
 - [GetErrorMapSuccessResponse](./Models/GetErrorMapSuccessResponse.md)
 - [GetEvaluationAnalyzerFailureResponse](./Models/GetEvaluationAnalyzerFailureResponse.md)
 - [GetEvaluationAnalyzerListFailureResponse](./Models/GetEvaluationAnalyzerListFailureResponse.md)
 - [GetEvaluationAnalyzerListReply](./Models/GetEvaluationAnalyzerListReply.md)
 - [GetEvaluationAnalyzerListSuccessResponse](./Models/GetEvaluationAnalyzerListSuccessResponse.md)
 - [GetEvaluationAnalyzerSuccessResponse](./Models/GetEvaluationAnalyzerSuccessResponse.md)
 - [GetEvaluationDetailFailureResponse](./Models/GetEvaluationDetailFailureResponse.md)
 - [GetEvaluationDetailSuccessResponse](./Models/GetEvaluationDetailSuccessResponse.md)
 - [GetEvaluationListFailureResponse](./Models/GetEvaluationListFailureResponse.md)
 - [GetEvaluationListReply](./Models/GetEvaluationListReply.md)
 - [GetEvaluationListSuccessResponse](./Models/GetEvaluationListSuccessResponse.md)
 - [GetEvaluationRecordBriefListFailureResponse](./Models/GetEvaluationRecordBriefListFailureResponse.md)
 - [GetEvaluationRecordBriefListReply](./Models/GetEvaluationRecordBriefListReply.md)
 - [GetEvaluationRecordBriefListSuccessResponse](./Models/GetEvaluationRecordBriefListSuccessResponse.md)
 - [GetEvaluationRecordFailureResponse](./Models/GetEvaluationRecordFailureResponse.md)
 - [GetEvaluationRecordSuccessResponse](./Models/GetEvaluationRecordSuccessResponse.md)
 - [GetEvaluationReleaseAnalyzerListFailureResponse](./Models/GetEvaluationReleaseAnalyzerListFailureResponse.md)
 - [GetEvaluationReleaseAnalyzerListReply](./Models/GetEvaluationReleaseAnalyzerListReply.md)
 - [GetEvaluationReleaseAnalyzerListSuccessResponse](./Models/GetEvaluationReleaseAnalyzerListSuccessResponse.md)
 - [GetEvaluationReleaseListFailureResponse](./Models/GetEvaluationReleaseListFailureResponse.md)
 - [GetEvaluationReleaseListReply](./Models/GetEvaluationReleaseListReply.md)
 - [GetEvaluationReleaseListSuccessResponse](./Models/GetEvaluationReleaseListSuccessResponse.md)
 - [GetEvaluationReleaseProtoFailureResponse](./Models/GetEvaluationReleaseProtoFailureResponse.md)
 - [GetEvaluationReleaseProtoReply](./Models/GetEvaluationReleaseProtoReply.md)
 - [GetEvaluationReleaseProtoSuccessResponse](./Models/GetEvaluationReleaseProtoSuccessResponse.md)
 - [GetEvaluationReleasePythonFailureResponse](./Models/GetEvaluationReleasePythonFailureResponse.md)
 - [GetEvaluationReleasePythonReply](./Models/GetEvaluationReleasePythonReply.md)
 - [GetEvaluationReleasePythonSuccessResponse](./Models/GetEvaluationReleasePythonSuccessResponse.md)
 - [GetFileDirectLinkFailureResponse](./Models/GetFileDirectLinkFailureResponse.md)
 - [GetFileDirectLinkReply](./Models/GetFileDirectLinkReply.md)
 - [GetFileDirectLinkSuccessResponse](./Models/GetFileDirectLinkSuccessResponse.md)
 - [GetNoticeFailureResponse](./Models/GetNoticeFailureResponse.md)
 - [GetNoticeSuccessResponse](./Models/GetNoticeSuccessResponse.md)
 - [GetPermissionFailureResponse](./Models/GetPermissionFailureResponse.md)
 - [GetPermissionSuccessResponse](./Models/GetPermissionSuccessResponse.md)
 - [GetRegistrationCodeListFailureResponse](./Models/GetRegistrationCodeListFailureResponse.md)
 - [GetRegistrationCodeListSuccessResponse](./Models/GetRegistrationCodeListSuccessResponse.md)
 - [GetScaleDetailFailureResponse](./Models/GetScaleDetailFailureResponse.md)
 - [GetScaleDetailSuccessResponse](./Models/GetScaleDetailSuccessResponse.md)
 - [GetScaleListFailureResponse](./Models/GetScaleListFailureResponse.md)
 - [GetScaleListSuccessResponse](./Models/GetScaleListSuccessResponse.md)
 - [GetSelfPermissionFailureResponse](./Models/GetSelfPermissionFailureResponse.md)
 - [GetSelfPermissionSuccessResponse](./Models/GetSelfPermissionSuccessResponse.md)
 - [GetSelfinfoFailureResponse](./Models/GetSelfinfoFailureResponse.md)
 - [GetSelfinfoSuccessResponse](./Models/GetSelfinfoSuccessResponse.md)
 - [GetStatusFailureResponse](./Models/GetStatusFailureResponse.md)
 - [GetStatusSuccessResponse](./Models/GetStatusSuccessResponse.md)
 - [GetSubjectBriefListFailureResponse](./Models/GetSubjectBriefListFailureResponse.md)
 - [GetSubjectBriefListReply](./Models/GetSubjectBriefListReply.md)
 - [GetSubjectBriefListSuccessResponse](./Models/GetSubjectBriefListSuccessResponse.md)
 - [GetSubjectDetailFailureResponse](./Models/GetSubjectDetailFailureResponse.md)
 - [GetSubjectDetailSuccessResponse](./Models/GetSubjectDetailSuccessResponse.md)
 - [GetTusConfigFailureResponse](./Models/GetTusConfigFailureResponse.md)
 - [GetUnitConfigFailureResponse](./Models/GetUnitConfigFailureResponse.md)
 - [GetUnitConfigSuccessResponse](./Models/GetUnitConfigSuccessResponse.md)
 - [GetUnitDetailFailureResponse](./Models/GetUnitDetailFailureResponse.md)
 - [GetUnitDetailReply](./Models/GetUnitDetailReply.md)
 - [GetUnitDetailSuccessResponse](./Models/GetUnitDetailSuccessResponse.md)
 - [GetUnitDeviceListFailureResponse](./Models/GetUnitDeviceListFailureResponse.md)
 - [GetUnitDeviceListSuccessResponse](./Models/GetUnitDeviceListSuccessResponse.md)
 - [GetUnitListFailureResponse](./Models/GetUnitListFailureResponse.md)
 - [GetUnitListReply](./Models/GetUnitListReply.md)
 - [GetUnitListSuccessResponse](./Models/GetUnitListSuccessResponse.md)
 - [GetUnitUserListFailureResponse](./Models/GetUnitUserListFailureResponse.md)
 - [GetUnitUserListSuccessResponse](./Models/GetUnitUserListSuccessResponse.md)
 - [GetUploadInfoFailureResponse](./Models/GetUploadInfoFailureResponse.md)
 - [GetUserConfigFailureResponse](./Models/GetUserConfigFailureResponse.md)
 - [GetUserConfigSuccessResponse](./Models/GetUserConfigSuccessResponse.md)
 - [GetUserSourceFailureResponse](./Models/GetUserSourceFailureResponse.md)
 - [GetUserSourceReply](./Models/GetUserSourceReply.md)
 - [GetUserSourceSuccessResponse](./Models/GetUserSourceSuccessResponse.md)
 - [GetUserinfoFailureResponse](./Models/GetUserinfoFailureResponse.md)
 - [GetUserinfoSuccessResponse](./Models/GetUserinfoSuccessResponse.md)
 - [GetWechatQrcodeResultFailureResponse](./Models/GetWechatQrcodeResultFailureResponse.md)
 - [GetWechatQrcodeResultReply](./Models/GetWechatQrcodeResultReply.md)
 - [GetWechatQrcodeResultSuccessResponse](./Models/GetWechatQrcodeResultSuccessResponse.md)
 - [LoginBody](./Models/LoginBody.md)
 - [LoginFailureResponse](./Models/LoginFailureResponse.md)
 - [LoginReply](./Models/LoginReply.md)
 - [LoginSuccessResponse](./Models/LoginSuccessResponse.md)
 - [OperaionResult](./Models/OperaionResult.md)
 - [ParameterValidatedErrorDetail](./Models/ParameterValidatedErrorDetail.md)
 - [Permission](./Models/Permission.md)
 - [PingFailureResponse](./Models/PingFailureResponse.md)
 - [PingSuccessResponse](./Models/PingSuccessResponse.md)
 - [RedirectFailureResponse](./Models/RedirectFailureResponse.md)
 - [RegisterBody](./Models/RegisterBody.md)
 - [RegisterDeviceBody](./Models/RegisterDeviceBody.md)
 - [RegisterDeviceFailureResponse](./Models/RegisterDeviceFailureResponse.md)
 - [RegisterDeviceReply](./Models/RegisterDeviceReply.md)
 - [RegisterDeviceSuccessResponse](./Models/RegisterDeviceSuccessResponse.md)
 - [RegisterFailureResponse](./Models/RegisterFailureResponse.md)
 - [RegisterSuccessResponse](./Models/RegisterSuccessResponse.md)
 - [RootFailureResponse](./Models/RootFailureResponse.md)
 - [RootSuccessResponse](./Models/RootSuccessResponse.md)
 - [ScaleRecordScopeType](./Models/ScaleRecordScopeType.md)
 - [ScaleScopeType](./Models/ScaleScopeType.md)
 - [SearchEvaluationRecordFailureResponse](./Models/SearchEvaluationRecordFailureResponse.md)
 - [SearchEvaluationRecordReply](./Models/SearchEvaluationRecordReply.md)
 - [SearchEvaluationRecordSearchSchema](./Models/SearchEvaluationRecordSearchSchema.md)
 - [SearchEvaluationRecordSearchSchema_create_time_inner](./Models/SearchEvaluationRecordSearchSchema_create_time_inner.md)
 - [SearchEvaluationRecordSearchSchema_update_time_inner](./Models/SearchEvaluationRecordSearchSchema_update_time_inner.md)
 - [SearchEvaluationRecordSuccessResponse](./Models/SearchEvaluationRecordSuccessResponse.md)
 - [SearchsubjectRecordFailureResponse](./Models/SearchsubjectRecordFailureResponse.md)
 - [SearchsubjectRecordReply](./Models/SearchsubjectRecordReply.md)
 - [SearchsubjectRecordSubjectSearchSchema](./Models/SearchsubjectRecordSubjectSearchSchema.md)
 - [SearchsubjectRecordSubjectSearchSchema_birthday_inner](./Models/SearchsubjectRecordSubjectSearchSchema_birthday_inner.md)
 - [SearchsubjectRecordSuccessResponse](./Models/SearchsubjectRecordSuccessResponse.md)
 - [SetSystemNoticeFailureResponse](./Models/SetSystemNoticeFailureResponse.md)
 - [SetSystemNoticeSuccessResponse](./Models/SetSystemNoticeSuccessResponse.md)
 - [SubjectBrief](./Models/SubjectBrief.md)
 - [SubjectDetail](./Models/SubjectDetail.md)
 - [SubjectScopeType](./Models/SubjectScopeType.md)
 - [UnitBrief](./Models/UnitBrief.md)
 - [UnitConfig](./Models/UnitConfig.md)
 - [UpdateEvaluationBody](./Models/UpdateEvaluationBody.md)
 - [UpdateEvaluationFailureResponse](./Models/UpdateEvaluationFailureResponse.md)
 - [UpdateEvaluationReleaseBody](./Models/UpdateEvaluationReleaseBody.md)
 - [UpdateEvaluationReleaseFailureResponse](./Models/UpdateEvaluationReleaseFailureResponse.md)
 - [UpdateEvaluationReleaseSuccessResponse](./Models/UpdateEvaluationReleaseSuccessResponse.md)
 - [UpdateEvaluationSuccessResponse](./Models/UpdateEvaluationSuccessResponse.md)
 - [UpdatePermissionBody](./Models/UpdatePermissionBody.md)
 - [UpdatePermissionFailureResponse](./Models/UpdatePermissionFailureResponse.md)
 - [UpdatePermissionSuccessResponse](./Models/UpdatePermissionSuccessResponse.md)
 - [UpdateSelfinfoFailureResponse](./Models/UpdateSelfinfoFailureResponse.md)
 - [UpdateSelfinfoSuccessResponse](./Models/UpdateSelfinfoSuccessResponse.md)
 - [UpdateSubjectBody](./Models/UpdateSubjectBody.md)
 - [UpdateSubjectFailureResponse](./Models/UpdateSubjectFailureResponse.md)
 - [UpdateSubjectSuccessResponse](./Models/UpdateSubjectSuccessResponse.md)
 - [UpdateUnitConfigFailureResponse](./Models/UpdateUnitConfigFailureResponse.md)
 - [UpdateUnitConfigSuccessResponse](./Models/UpdateUnitConfigSuccessResponse.md)
 - [UpdateUnitInfoBody](./Models/UpdateUnitInfoBody.md)
 - [UpdateUnitInfoFailureResponse](./Models/UpdateUnitInfoFailureResponse.md)
 - [UpdateUnitInfoSuccessResponse](./Models/UpdateUnitInfoSuccessResponse.md)
 - [UpdateUserConfigFailureResponse](./Models/UpdateUserConfigFailureResponse.md)
 - [UpdateUserConfigSuccessResponse](./Models/UpdateUserConfigSuccessResponse.md)
 - [UpdateUserinfoBody](./Models/UpdateUserinfoBody.md)
 - [UpdateUserinfoFailureResponse](./Models/UpdateUserinfoFailureResponse.md)
 - [UpdateUserinfoSuccessResponse](./Models/UpdateUserinfoSuccessResponse.md)
 - [UploadEvaluationRecordBody](./Models/UploadEvaluationRecordBody.md)
 - [UploadEvaluationRecordFailureResponse](./Models/UploadEvaluationRecordFailureResponse.md)
 - [UploadEvaluationRecordSuccessResponse](./Models/UploadEvaluationRecordSuccessResponse.md)
 - [UploadFileChunkFailureResponse](./Models/UploadFileChunkFailureResponse.md)
 - [UploadFilePrecheckBody](./Models/UploadFilePrecheckBody.md)
 - [UploadFilePrecheckFailureResponse](./Models/UploadFilePrecheckFailureResponse.md)
 - [UploadFilePrecheckReply](./Models/UploadFilePrecheckReply.md)
 - [UploadFilePrecheckSuccessResponse](./Models/UploadFilePrecheckSuccessResponse.md)
 - [UserClientConfig](./Models/UserClientConfig.md)
 - [UserConfig](./Models/UserConfig.md)
 - [UserInfo](./Models/UserInfo.md)
 - [WeChatAuthorizeFailureResponse](./Models/WeChatAuthorizeFailureResponse.md)
 - [WeChatLoginBody](./Models/WeChatLoginBody.md)
 - [WeChatLoginFailureResponse](./Models/WeChatLoginFailureResponse.md)
 - [WeChatLoginReply](./Models/WeChatLoginReply.md)
 - [WeChatLoginSuccessResponse](./Models/WeChatLoginSuccessResponse.md)
 - [WechatAccessFailureResponse](./Models/WechatAccessFailureResponse.md)
 - [WechatHandleFailureResponse](./Models/WechatHandleFailureResponse.md)


<a name="documentation-for-authorization"></a>
## Documentation for Authorization

<a name="AuthHeader"></a>
### AuthHeader

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header

<a name="SignHeader"></a>
### SignHeader

- **Type**: API key
- **API key parameter name**: Signature
- **Location**: HTTP header

