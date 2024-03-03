# 导览

## 平台简介 { #introduction }

**`多模态大数据采集与分析平台`**是由[TCMX团队](#team)开发的一套服务体系，用户主要以[**`客户端`**](client/index.md)作为使用入口，通过它，数据的采集、分析、展示、管理等功能所见即所得。

为了解决我们日常研究时在数据采集过程遇到的难题，我们于2021年底开发了一款内部集成了多维度数据采集功能的桌面端程序。
该程序仅实现了对我们当时为数不多的几个范式的数据采集，以及对数据在本地进行简单的管理这两个功能，但它已经为我们的研究工作提供了不小的便利。
在后来的两年内我们持续对该程序进行了开发，引入了后端服务，也加入了更多的范式，它也渐渐描述出了如今的平台的轮廓，这便是本平台的前身。
鉴于该程序初期并未考虑太多，我们于2023年6月重新开发了该平台，并将其正式命名为**`多模态大数据采集与分析平台`**。

## 平台构成 { #constitute }

平台主要由[**`客户端`**](client/index.md)与[**`服务端`**](server/index.md)两个部件构成，二者之间通过HTTPS网络请求进行通信。

<figure id="constitute">
    <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" width="491px" height="121px" viewBox="-0.5 -0.5 491 121"><defs/><g><a xlink:href="server"><g><path d="M 362.5 45 C 328.5 45 320 70 347.2 75 C 320 86 350.6 110 372.7 100 C 388 120 439 120 456 100 C 490 100 490 80 468.75 70 C 490 50 456 30 426.25 40 C 405 25 371 25 362.5 45 Z" fill="rgb(255, 255, 255)" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="all"/></g><g><g transform="translate(-0.5 -0.5)"><switch><foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 168px; height: 1px; padding-top: 70px; margin-left: 321px;"><div data-drawio-colors="color: rgb(0, 0, 0); " style="box-sizing: border-box; font-size: 0px; text-align: center;"><div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; white-space: normal; overflow-wrap: normal;">数据中心（服务端）</div></div></div></foreignObject><text x="405" y="74" fill="rgb(0, 0, 0)" font-family="Helvetica" font-size="12px" text-anchor="middle">数据中心（服务端）</text></switch></g></g></a><a xlink:href="client"><g><path d="M 0 23 L 0 0 L 210 0 L 210 23" fill="rgb(255, 255, 255)" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="all"/><path d="M 0 23 L 0 120 L 210 120 L 210 23" fill="none" stroke="rgb(0, 0, 0)" stroke-miterlimit="10"/><path d="M 0 23 L 210 23" fill="none" stroke="rgb(0, 0, 0)" stroke-miterlimit="10"/></g><g><g transform="translate(-0.5 -0.5)"><switch><foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 208px; height: 1px; padding-top: 12px; margin-left: 1px;"><div data-drawio-colors="color: rgb(0, 0, 0); " style="box-sizing: border-box; font-size: 0px; text-align: center;"><div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; font-weight: bold; white-space: normal; overflow-wrap: normal;">数据采集与分析控制面板（客户端）</div></div></div></foreignObject><text x="105" y="15" fill="rgb(0, 0, 0)" font-family="Helvetica" font-size="12px" text-anchor="middle" font-weight="bold">数据采集与分析控制面板（客户端）</text></switch></g></g></a><a xlink:href="sdk"><g><path d="M 47 50 C 47 41.72 72.97 35 105 35 C 120.38 35 135.14 36.58 146.01 39.39 C 156.89 42.21 163 46.02 163 50 L 163 90 C 163 98.28 137.03 105 105 105 C 72.97 105 47 98.28 47 90 Z" fill="rgb(255, 255, 255)" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="all"/><path d="M 163 50 C 163 58.28 137.03 65 105 65 C 72.97 65 47 58.28 47 50" fill="none" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="all"/></g><g><g transform="translate(-0.5 -0.5)"><switch><foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 114px; height: 1px; padding-top: 83px; margin-left: 48px;"><div data-drawio-colors="color: rgb(0, 0, 0); " style="box-sizing: border-box; font-size: 0px; text-align: center;"><div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; white-space: normal; overflow-wrap: normal;">SDK</div></div></div></foreignObject><text x="105" y="86" fill="rgb(0, 0, 0)" font-family="Helvetica" font-size="12px" text-anchor="middle">SDK</text></switch></g></g></a><g><path d="M 163 70 L 325.7 68.75" fill="none" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="stroke"/><path d="M 330.95 68.71 L 323.98 72.26 L 325.7 68.75 L 323.93 65.26 Z" fill="rgb(0, 0, 0)" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="all"/></g><g><g transform="translate(-0.5 -0.5)"><switch><foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 1px; height: 1px; padding-top: 70px; margin-left: 248px;"><div data-drawio-colors="color: rgb(0, 0, 0); background-color: rgb(255, 255, 255); " style="box-sizing: border-box; font-size: 0px; text-align: center;"><div style="display: inline-block; font-size: 11px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; background-color: rgb(255, 255, 255); white-space: nowrap;">Label</div></div></div></foreignObject><text x="248" y="73" fill="rgb(0, 0, 0)" font-family="Helvetica" font-size="11px" text-anchor="middle">Label</text></switch></g></g><g><g transform="translate(-0.5 -0.5)"><switch><foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 1px; height: 1px; padding-top: 71px; margin-left: 248px;"><div data-drawio-colors="color: rgb(0, 0, 0); background-color: rgb(255, 255, 255); " style="box-sizing: border-box; font-size: 0px; text-align: center;"><div style="display: inline-block; font-size: 11px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; background-color: rgb(255, 255, 255); white-space: nowrap;">  HTTPS  </div></div></div></foreignObject><text x="248" y="74" fill="rgb(0, 0, 0)" font-family="Helvetica" font-size="11px" text-anchor="middle">  HTTPS  </text></switch></g></g></g><switch><g requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"/><a transform="translate(0,-5)" xlink:href="https://www.drawio.com/doc/faq/svg-export-text-problems" target="_blank"><text text-anchor="middle" font-size="10px" x="50%" y="100%">Text is not SVG - cannot display</text></a></switch></svg>
    <figcaption>平台架构图</figcaption>
</figure>
-----

[平台架构图](#constitute)显示，在客户端中我们包含了[**`SDK`**](sdk/index.md)，这也是本平台的一部分。

## 平台特性 { #feature .annotate }

- 客户端使用简单易懂的交互方式，实现了强大的数据采集、管理功能
- 服务端采用分布式架构，能够实现高并发、高可用、高冗余
- 平台支持多种数据维度，并且能够轻松地对数据维度进行扩展
- 不限数据大小，不限数据来源，不限数据格式
- 支持纯SDK接入，拥有无限可能
- 支持本地/云端对数据进行分析，也可将海量计算分析任务编排，由服务端进行处理
- 客户端提供了多种数据可视化的方式，并支持数据导入、导出

??? tip "提示"
    上述部分功能仍在开发中

## 团队介绍 { #team }

该平台由TCMX团队开发，团队成员包括：

- 张三
- 李四
- 王五

## 联系我们 { #contact }

如果您有任何问题或建议，请随时联系我们。

邮箱：<tcmx@zcmu.edu.com>

## 下载 { #download }

[最新客户端 :material-download:](index.md){ .md-button }

[历史版本](index.md)
