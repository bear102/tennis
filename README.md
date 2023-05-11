<!DOCTYPE html>
<!-- saved from url=(0051)https://pypi.org/project/tennis/0.1.2/#2-tiebreaker -->
<html lang="en" dir="ltr"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <meta name="defaultLanguage" content="en">
    <meta name="availableLanguages" content="en, es, fr, ja, pt_BR, uk, el, de, zh_Hans, zh_Hant, ru, he, eo">

    

    <title>tennis · PyPI</title>
    <meta name="description" content="A library for tracking tennis matches and scoring">

    <link rel="stylesheet" href="./rm_files/warehouse-ltr.332cdbbf.css">
    <link rel="stylesheet" href="./rm_files/fontawesome.ac611abc.css">
    <link rel="stylesheet" href="./rm_files/css">
    <noscript>
      <link rel="stylesheet" href="/static/css/noscript.0673c9ea.css">
    </noscript>

    

    <link rel="icon" href="https://pypi.org/static/images/favicon.35549fe8.ico" type="image/x-icon">

    <link rel="alternate" type="application/rss+xml" title="RSS: 40 latest updates" href="https://pypi.org/rss/updates.xml">
    <link rel="alternate" type="application/rss+xml" title="RSS: 40 newest packages" href="https://pypi.org/rss/packages.xml">
    <link rel="alternate" type="application/rss+xml" title="RSS: latest releases for tennis" href="https://pypi.org/rss/project/tennis/releases.xml">
    
    <link rel="canonical" href="https://pypi.org/project/tennis/">
    

    <meta property="og:url" content="https://pypi.org/project/tennis/0.1.2/">
    <meta property="og:site_name" content="PyPI">
    <meta property="og:type" content="website">
    <meta property="og:image" content="https://pypi.org/static/images/twitter.abaf4b19.webp">
    <meta property="og:title" content="tennis">
    <meta property="og:description" content="A library for tracking tennis matches and scoring">
    

<meta name="googlebot" content="noindex">



    <link rel="search" type="application/opensearchdescription+xml" title="PyPI" href="https://pypi.org/opensearch.xml">

    
    <script type="text/javascript" async="" src="./rm_files/analytics.js.download"></script><script type="text/javascript" async="" src="./rm_files/js"></script><script async="" data-ga-id="UA-55961911-1" data-ga4-id="G-RW7D75DF8V" src="./rm_files/warehouse.7aabb880.js.download">
    </script>
    
<script>
MathJax = {
  tex: {
    inlineMath: [['$', '$'], ['\\(', '\\)']]
  },
};
</script>
<script async="" src="./rm_files/tex-svg.js.download" integrity="sha256-1CldwzdEg2k1wTmf7s5RWVd7NMXI/7nxxjJM2C4DqII=" crossorigin="anonymous"></script>

    <script async="" src="./rm_files/js(1)"></script>
    <script async="" src="./rm_files/js(2)"></script>
    <script defer="" src="./rm_files/insights.js.download"></script>
    <script async="" src="./rm_files/ethicalads.min.js.download" integrity="sha256-U3hKDidudIaxBDEzwGJApJgPEf2mWk6cfMWghrAa6i0= sha384-UcmsCqcNRSLW/dV3Lo1oCi2/VaurXbib6p4HyUEOeIa/4OpsrnucrugAefzVZJfI sha512-q4t1L4xEjGV2R4hzqCa41P8jrgFUS8xTb8rdNv4FGvw7FpydVj/kkxBJHOiaoxHa8olCcx1Slk9K+3sNbsM4ug==" crossorigin="anonymous"></script>

    
  <style type="text/css">.CtxtMenu_InfoClose {  top:.2em; right:.2em;}
.CtxtMenu_InfoContent {  overflow:auto; text-align:left; font-size:80%;  padding:.4em .6em; border:1px inset; margin:1em 0px;  max-height:20em; max-width:30em; background-color:#EEEEEE;  white-space:normal;}
.CtxtMenu_Info.CtxtMenu_MousePost {outline:none;}
.CtxtMenu_Info {  position:fixed; left:50%; width:auto; text-align:center;  border:3px outset; padding:1em 2em; background-color:#DDDDDD;  color:black;  cursor:default; font-family:message-box; font-size:120%;  font-style:normal; text-indent:0; text-transform:none;  line-height:normal; letter-spacing:normal; word-spacing:normal;  word-wrap:normal; white-space:nowrap; float:none; z-index:201;  border-radius: 15px;                     /* Opera 10.5 and IE9 */  -webkit-border-radius:15px;               /* Safari and Chrome */  -moz-border-radius:15px;                  /* Firefox */  -khtml-border-radius:15px;                /* Konqueror */  box-shadow:0px 10px 20px #808080;         /* Opera 10.5 and IE9 */  -webkit-box-shadow:0px 10px 20px #808080; /* Safari 3 & Chrome */  -moz-box-shadow:0px 10px 20px #808080;    /* Forefox 3.5 */  -khtml-box-shadow:0px 10px 20px #808080;  /* Konqueror */  filter:progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color="gray", Positive="true"); /* IE */}
</style><style type="text/css">.CtxtMenu_MenuClose {  position:absolute;  cursor:pointer;  display:inline-block;  border:2px solid #AAA;  border-radius:18px;  -webkit-border-radius: 18px;             /* Safari and Chrome */  -moz-border-radius: 18px;                /* Firefox */  -khtml-border-radius: 18px;              /* Konqueror */  font-family: "Courier New", Courier;  font-size:24px;  color:#F0F0F0}
.CtxtMenu_MenuClose span {  display:block; background-color:#AAA; border:1.5px solid;  border-radius:18px;  -webkit-border-radius: 18px;             /* Safari and Chrome */  -moz-border-radius: 18px;                /* Firefox */  -khtml-border-radius: 18px;              /* Konqueror */  line-height:0;  padding:8px 0 6px     /* may need to be browser-specific */}
.CtxtMenu_MenuClose:hover {  color:white!important;  border:2px solid #CCC!important}
.CtxtMenu_MenuClose:hover span {  background-color:#CCC!important}
.CtxtMenu_MenuClose:hover:focus {  outline:none}
</style><style type="text/css">.CtxtMenu_Menu {  position:absolute;  background-color:white;  color:black;  width:auto; padding:5px 0px;  border:1px solid #CCCCCC; margin:0; cursor:default;  font: menu; text-align:left; text-indent:0; text-transform:none;  line-height:normal; letter-spacing:normal; word-spacing:normal;  word-wrap:normal; white-space:nowrap; float:none; z-index:201;  border-radius: 5px;                     /* Opera 10.5 and IE9 */  -webkit-border-radius: 5px;             /* Safari and Chrome */  -moz-border-radius: 5px;                /* Firefox */  -khtml-border-radius: 5px;              /* Konqueror */  box-shadow:0px 10px 20px #808080;         /* Opera 10.5 and IE9 */  -webkit-box-shadow:0px 10px 20px #808080; /* Safari 3 & Chrome */  -moz-box-shadow:0px 10px 20px #808080;    /* Forefox 3.5 */  -khtml-box-shadow:0px 10px 20px #808080;  /* Konqueror */}
.CtxtMenu_MenuItem {  padding: 1px 2em;  background:transparent;}
.CtxtMenu_MenuArrow {  position:absolute; right:.5em; padding-top:.25em; color:#666666;  font-family: null; font-size: .75em}
.CtxtMenu_MenuActive .CtxtMenu_MenuArrow {color:white}
.CtxtMenu_MenuArrow.CtxtMenu_RTL {left:.5em; right:auto}
.CtxtMenu_MenuCheck {  position:absolute; left:.7em;  font-family: null}
.CtxtMenu_MenuCheck.CtxtMenu_RTL { right:.7em; left:auto }
.CtxtMenu_MenuRadioCheck {  position:absolute; left: .7em;}
.CtxtMenu_MenuRadioCheck.CtxtMenu_RTL {  right: .7em; left:auto}
.CtxtMenu_MenuInputBox {  padding-left: 1em; right:.5em; color:#666666;  font-family: null;}
.CtxtMenu_MenuInputBox.CtxtMenu_RTL {  left: .1em;}
.CtxtMenu_MenuComboBox {  left:.1em; padding-bottom:.5em;}
.CtxtMenu_MenuSlider {  left: .1em;}
.CtxtMenu_SliderValue {  position:absolute; right:.1em; padding-top:.25em; color:#333333;  font-size: .75em}
.CtxtMenu_SliderBar {  outline: none; background: #d3d3d3}
.CtxtMenu_MenuLabel {  padding: 1px 2em 3px 1.33em;  font-style:italic}
.CtxtMenu_MenuRule {  border-top: 1px solid #DDDDDD;  margin: 4px 3px;}
.CtxtMenu_MenuDisabled {  color:GrayText}
.CtxtMenu_MenuActive {  background-color: #606872;  color: white;}
.CtxtMenu_MenuDisabled:focus {  background-color: #E8E8E8}
.CtxtMenu_MenuLabel:focus {  background-color: #E8E8E8}
.CtxtMenu_ContextMenu:focus {  outline:none}
.CtxtMenu_ContextMenu .CtxtMenu_MenuItem:focus {  outline:none}
.CtxtMenu_SelectionMenu {  position:relative; float:left;  border-bottom: none; -webkit-box-shadow:none; -webkit-border-radius:0px; }
.CtxtMenu_SelectionItem {  padding-right: 1em;}
.CtxtMenu_Selection {  right: 40%; width:50%; }
.CtxtMenu_SelectionBox {  padding: 0em; max-height:20em; max-width: none;  background-color:#FFFFFF;}
.CtxtMenu_SelectionDivider {  clear: both; border-top: 2px solid #000000;}
.CtxtMenu_Menu .CtxtMenu_MenuClose {  top:-10px; left:-10px}
</style><style id="MJX-SVG-styles">
mjx-container[jax="SVG"] {
  direction: ltr;
}

mjx-container[jax="SVG"] > svg {
  overflow: visible;
  min-height: 1px;
  min-width: 1px;
}

mjx-container[jax="SVG"] > svg a {
  fill: blue;
  stroke: blue;
}

mjx-assistive-mml {
  position: absolute !important;
  top: 0px;
  left: 0px;
  clip: rect(1px, 1px, 1px, 1px);
  padding: 1px 0px 0px 0px !important;
  border: 0px !important;
  display: block !important;
  width: auto !important;
  overflow: hidden !important;
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

mjx-assistive-mml[display="block"] {
  width: 100% !important;
}

mjx-container[jax="SVG"][display="true"] {
  display: block;
  text-align: center;
  margin: 1em 0;
}

mjx-container[jax="SVG"][display="true"][width="full"] {
  display: flex;
}

mjx-container[jax="SVG"][justify="left"] {
  text-align: left;
}

mjx-container[jax="SVG"][justify="right"] {
  text-align: right;
}

g[data-mml-node="merror"] > g {
  fill: red;
  stroke: red;
}

g[data-mml-node="merror"] > rect[data-background] {
  fill: yellow;
  stroke: none;
}

g[data-mml-node="mtable"] > line[data-line], svg[data-table] > g > line[data-line] {
  stroke-width: 70px;
  fill: none;
}

g[data-mml-node="mtable"] > rect[data-frame], svg[data-table] > g > rect[data-frame] {
  stroke-width: 70px;
  fill: none;
}

g[data-mml-node="mtable"] > .mjx-dashed, svg[data-table] > g > .mjx-dashed {
  stroke-dasharray: 140;
}

g[data-mml-node="mtable"] > .mjx-dotted, svg[data-table] > g > .mjx-dotted {
  stroke-linecap: round;
  stroke-dasharray: 0,140;
}

g[data-mml-node="mtable"] > g > svg {
  overflow: visible;
}

[jax="SVG"] mjx-tool {
  display: inline-block;
  position: relative;
  width: 0;
  height: 0;
}

[jax="SVG"] mjx-tool > mjx-tip {
  position: absolute;
  top: 0;
  left: 0;
}

mjx-tool > mjx-tip {
  display: inline-block;
  padding: .2em;
  border: 1px solid #888;
  font-size: 70%;
  background-color: #F8F8F8;
  color: black;
  box-shadow: 2px 2px 5px #AAAAAA;
}

g[data-mml-node="maction"][data-toggle] {
  cursor: pointer;
}

mjx-status {
  display: block;
  position: fixed;
  left: 1em;
  bottom: 1em;
  min-width: 25%;
  padding: .2em .4em;
  border: 1px solid #888;
  font-size: 90%;
  background-color: #F8F8F8;
  color: black;
}

foreignObject[data-mjx-xml] {
  font-family: initial;
  line-height: normal;
  overflow: visible;
}

mjx-container[jax="SVG"] path[data-c], mjx-container[jax="SVG"] use[data-c] {
  stroke-width: 3;
}
</style><style>[data-ea-publisher].loaded,[data-ea-type].loaded{font-size:14px;font-family:-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, Noto Sans, sans-serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji;font-weight:normal;font-style:normal;leter-spacing:0px;vertical-align:baseline;line-height:1.3em}[data-ea-publisher].loaded a,[data-ea-type].loaded a{text-decoration:none}[data-ea-publisher].loaded .ea-pixel,[data-ea-type].loaded .ea-pixel{display:none}[data-ea-publisher].loaded .ea-content,[data-ea-type].loaded .ea-content{margin:1em 1em 0.5em 1em;padding:1em;background:rgba(0,0,0,0.03);color:#505050}[data-ea-publisher].loaded .ea-content a:link,[data-ea-type].loaded .ea-content a:link{color:#505050}[data-ea-publisher].loaded .ea-content a:visited,[data-ea-type].loaded .ea-content a:visited{color:#505050}[data-ea-publisher].loaded .ea-content a:hover,[data-ea-type].loaded .ea-content a:hover{color:#373737}[data-ea-publisher].loaded .ea-content a:active,[data-ea-type].loaded .ea-content a:active{color:#373737}[data-ea-publisher].loaded .ea-content a strong,[data-ea-publisher].loaded .ea-content a b,[data-ea-type].loaded .ea-content a strong,[data-ea-type].loaded .ea-content a b{color:#088cdb}[data-ea-publisher].loaded .ea-callout a:link,[data-ea-type].loaded .ea-callout a:link{color:#6a6a6a}[data-ea-publisher].loaded .ea-callout a:visited,[data-ea-type].loaded .ea-callout a:visited{color:#6a6a6a}[data-ea-publisher].loaded .ea-callout a:hover,[data-ea-type].loaded .ea-callout a:hover{color:#505050}[data-ea-publisher].loaded .ea-callout a:active,[data-ea-type].loaded .ea-callout a:active{color:#505050}[data-ea-publisher].loaded .ea-callout a strong,[data-ea-publisher].loaded .ea-callout a b,[data-ea-type].loaded .ea-callout a strong,[data-ea-type].loaded .ea-callout a b{color:#088cdb}[data-ea-publisher].loaded .ea-callout a,[data-ea-type].loaded .ea-callout a{font-size:0.8em}[data-ea-publisher].loaded.dark .ea-content,[data-ea-type].loaded.dark .ea-content{background:rgba(255,255,255,0.05);color:#dcdcdc}[data-ea-publisher].loaded.dark .ea-content a:link,[data-ea-type].loaded.dark .ea-content a:link{color:#dcdcdc}[data-ea-publisher].loaded.dark .ea-content a:visited,[data-ea-type].loaded.dark .ea-content a:visited{color:#dcdcdc}[data-ea-publisher].loaded.dark .ea-content a:hover,[data-ea-type].loaded.dark .ea-content a:hover{color:#f6f6f6}[data-ea-publisher].loaded.dark .ea-content a:active,[data-ea-type].loaded.dark .ea-content a:active{color:#f6f6f6}[data-ea-publisher].loaded.dark .ea-content a strong,[data-ea-publisher].loaded.dark .ea-content a b,[data-ea-type].loaded.dark .ea-content a strong,[data-ea-type].loaded.dark .ea-content a b{color:#50baf9}[data-ea-publisher].loaded.dark .ea-callout a:link,[data-ea-type].loaded.dark .ea-callout a:link{color:#c3c3c3}[data-ea-publisher].loaded.dark .ea-callout a:visited,[data-ea-type].loaded.dark .ea-callout a:visited{color:#c3c3c3}[data-ea-publisher].loaded.dark .ea-callout a:hover,[data-ea-type].loaded.dark .ea-callout a:hover{color:#dcdcdc}[data-ea-publisher].loaded.dark .ea-callout a:active,[data-ea-type].loaded.dark .ea-callout a:active{color:#dcdcdc}[data-ea-publisher].loaded.dark .ea-callout a strong,[data-ea-publisher].loaded.dark .ea-callout a b,[data-ea-type].loaded.dark .ea-callout a strong,[data-ea-type].loaded.dark .ea-callout a b{color:#50baf9}@media (prefers-color-scheme: dark){[data-ea-publisher].loaded.adaptive .ea-content,[data-ea-type].loaded.adaptive .ea-content{background:rgba(255,255,255,0.05);color:#dcdcdc}[data-ea-publisher].loaded.adaptive .ea-content a:link,[data-ea-type].loaded.adaptive .ea-content a:link{color:#dcdcdc}[data-ea-publisher].loaded.adaptive .ea-content a:visited,[data-ea-type].loaded.adaptive .ea-content a:visited{color:#dcdcdc}[data-ea-publisher].loaded.adaptive .ea-content a:hover,[data-ea-type].loaded.adaptive .ea-content a:hover{color:#f6f6f6}[data-ea-publisher].loaded.adaptive .ea-content a:active,[data-ea-type].loaded.adaptive .ea-content a:active{color:#f6f6f6}[data-ea-publisher].loaded.adaptive .ea-content a strong,[data-ea-publisher].loaded.adaptive .ea-content a b,[data-ea-type].loaded.adaptive .ea-content a strong,[data-ea-type].loaded.adaptive .ea-content a b{color:#50baf9}[data-ea-publisher].loaded.adaptive .ea-callout a:link,[data-ea-type].loaded.adaptive .ea-callout a:link{color:#c3c3c3}[data-ea-publisher].loaded.adaptive .ea-callout a:visited,[data-ea-type].loaded.adaptive .ea-callout a:visited{color:#c3c3c3}[data-ea-publisher].loaded.adaptive .ea-callout a:hover,[data-ea-type].loaded.adaptive .ea-callout a:hover{color:#dcdcdc}[data-ea-publisher].loaded.adaptive .ea-callout a:active,[data-ea-type].loaded.adaptive .ea-callout a:active{color:#dcdcdc}[data-ea-publisher].loaded.adaptive .ea-callout a strong,[data-ea-publisher].loaded.adaptive .ea-callout a b,[data-ea-type].loaded.adaptive .ea-callout a strong,[data-ea-type].loaded.adaptive .ea-callout a b{color:#50baf9}}[data-ea-publisher].loaded .ea-content,[data-ea-type].loaded .ea-content{border:0px;border-radius:3px;box-shadow:0px 2px 3px rgba(0,0,0,0.15)}[data-ea-publisher].loaded.raised .ea-content,[data-ea-type].loaded.raised .ea-content{border:0px;border-radius:3px;box-shadow:0px 2px 3px rgba(0,0,0,0.15)}[data-ea-publisher].loaded.bordered .ea-content,[data-ea-type].loaded.bordered .ea-content{border:1px solid rgba(0,0,0,0.04);border-radius:3px;box-shadow:none}[data-ea-publisher].loaded.bordered.dark .ea-content,[data-ea-type].loaded.bordered.dark .ea-content{border:1px solid rgba(255,255,255,0.07)}@media (prefers-color-scheme: dark){[data-ea-publisher].loaded.bordered.adaptive .ea-content,[data-ea-type].loaded.bordered.adaptive .ea-content{border:1px solid rgba(255,255,255,0.07)}}[data-ea-publisher].loaded.flat .ea-content,[data-ea-type].loaded.flat .ea-content{border:0px;border-radius:3px;box-shadow:none}[data-ea-type="image"].loaded,[data-ea-publisher]:not([data-ea-type]).loaded,.ea-type-image{display:inline-block}[data-ea-type="image"].loaded .ea-content,[data-ea-publisher]:not([data-ea-type]).loaded .ea-content,.ea-type-image .ea-content{max-width:180px;overflow:auto;text-align:center}[data-ea-type="image"].loaded .ea-content>a>img,[data-ea-publisher]:not([data-ea-type]).loaded .ea-content>a>img,.ea-type-image .ea-content>a>img{width:120px;height:90px;display:inline-block}[data-ea-type="image"].loaded .ea-content>.ea-text,[data-ea-publisher]:not([data-ea-type]).loaded .ea-content>.ea-text,.ea-type-image .ea-content>.ea-text{margin-top:1em;font-size:1em;text-align:center}[data-ea-type="image"].loaded .ea-callout,[data-ea-publisher]:not([data-ea-type]).loaded .ea-callout,.ea-type-image .ea-callout{max-width:180px;margin:0em 1em 1em 1em;padding-left:1em;padding-right:1em;font-style:italic;text-align:right}[data-ea-type="image"].loaded.horizontal .ea-content,[data-ea-publisher]:not([data-ea-type]).loaded.horizontal .ea-content,.ea-type-image.horizontal .ea-content{max-width:320px}[data-ea-type="image"].loaded.horizontal .ea-content>a>img,[data-ea-publisher]:not([data-ea-type]).loaded.horizontal .ea-content>a>img,.ea-type-image.horizontal .ea-content>a>img{float:left;margin-right:1em}[data-ea-type="image"].loaded.horizontal .ea-content .ea-text,[data-ea-publisher]:not([data-ea-type]).loaded.horizontal .ea-content .ea-text,.ea-type-image.horizontal .ea-content .ea-text{margin-top:0em;text-align:left;overflow:auto}[data-ea-type="image"].loaded.horizontal .ea-callout,[data-ea-publisher]:not([data-ea-type]).loaded.horizontal .ea-callout,.ea-type-image.horizontal .ea-callout{max-width:320px;text-align:right}[data-ea-type="text"].loaded,.ea-type-text{font-size:14px}[data-ea-type="text"].loaded .ea-content,.ea-type-text .ea-content{text-align:left}[data-ea-type="text"].loaded .ea-callout,.ea-type-text .ea-callout{margin:0.5em 1em 1em 1em;padding-left:1em;padding-right:1em;text-align:right;font-style:italic}[data-ea-style="stickybox"].loaded .ea-type-image{z-index:1000;position:fixed;bottom:20px;right:20px}[data-ea-style="stickybox"].loaded .ea-type-image .ea-stickybox-hide{cursor:pointer;position:absolute;top:0.75em;right:0.75em;background-color:#fefefe;border:1px solid #088cdb;border-radius:50%;color:#088cdb;font-size:1em;text-align:center;height:1.5em;width:1.5em;line-height:1.5em}@media (max-width: 1300px){[data-ea-style="stickybox"].loaded .ea-type-image{position:static;bottom:0;right:0;margin:auto;text-align:center}[data-ea-style="stickybox"].loaded .ea-type-image .ea-stickybox-hide{display:none}}@media (min-width: 1301px){[data-ea-style="stickybox"].loaded .ea-type-image .ea-content{background:#dcdcdc}[data-ea-style="stickybox"].loaded.dark .ea-type-image .ea-content{background:#505050}}@media (min-width: 1301px) and (prefers-color-scheme: dark){[data-ea-style="stickybox"].loaded.adaptive .ea-type-image .ea-content{background:#505050}}
</style><script src="./rm_files/saved_resource" type="text/javascript" async=""></script></head>

  <body data-controller="viewport-toggle" style="padding-top: 0px;">
    

    <!-- Accessibility: this link should always be the first piece of content inside the body-->
    <a href="https://pypi.org/project/tennis/0.1.2/#content" class="skip-to-content">Skip to main content</a>

    <button type="button" class="button button--primary button--switch-to-mobile hidden" data-viewport-toggle-target="switchToMobile" data-action="viewport-toggle#switchToMobile">
      Switch to mobile version
    </button>

    <div id="sticky-notifications" class="stick-to-top js-stick-to-top">
      <!-- Add browser warning. Will show for ie9 and below -->
      <!--[if IE]>
      <div class="notification-bar notification-bar--warning" role="status">
        <span class="notification-bar__icon">
          <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
          <span class="sr-only">Warning</span>
        </span>
        <span class="notification-bar__message">You are using an unsupported browser, upgrade to a newer version.</span>
      </div>
      <![endif]-->
      
      <noscript>
      <div class="notification-bar notification-bar--warning" role="status">
        
        <span class="notification-bar__icon">
          <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
          <span class="sr-only">Warning</span>
        </span>
        <span class="notification-bar__message">Some features may not work without JavaScript. Please try enabling it if you encounter problems.</span>
      </div>
      </noscript>

      
        <div data-html-include="/_includes/notification-banners/"></div>
      
    </div>

    
      <div data-html-include="/_includes/flash-messages/">





</div>
    

    

    
      <div data-html-include="/_includes/session-notifications/"></div>
    

    <header class="site-header ">
      <div class="site-container">
        <div class="split-layout">
          
          <div class="split-layout">
            <div>
              <a class="site-header__logo" href="https://pypi.org/">
                <img alt="PyPI" src="./rm_files/logo-small.2a411bc6.svg">
              </a>
            </div>

            <form class="search-form search-form--primary" action="https://pypi.org/search/" role="search">
              <label for="search" class="sr-only">Search PyPI</label>
              <input id="search" class="search-form__search" type="text" name="q" placeholder="Search projects" value="" autocomplete="off" autocapitalize="off" spellcheck="false" data-controller="search-focus" data-action="keydown@window-&gt;search-focus#focusSearchField" data-search-focus-target="searchField">
              
              <button type="submit" class="search-form__button">
                <i class="fa fa-search" aria-hidden="true"></i>
                <span class="sr-only">Search</span>
              </button>
            </form>
          </div>
          

          <div data-html-include="/_includes/current-user-indicator/">
    
    <div id="user-indicator" class="horizontal-menu horizontal-menu--light horizontal-menu--tall">
  <nav class="horizontal-menu horizontal-menu--light horizontal-menu--tall hide-on-tablet" aria-label="Main navigation">
    <ul>
      <li class="horizontal-menu__item"><a href="https://pypi.org/help/" class="horizontal-menu__link">Help</a></li>
      <li class="horizontal-menu__item"><a href="https://pypi.org/sponsors/" class="horizontal-menu__link">Sponsors</a></li>
      <li class="horizontal-menu__item"><a href="https://pypi.org/account/login/" class="horizontal-menu__link">Log in</a></li>
      <li class="horizontal-menu__item"><a href="https://pypi.org/account/register/" class="horizontal-menu__link">Register</a></li>
    </ul>
  </nav>
  <nav class="dropdown dropdown--on-menu hidden show-on-tablet" aria-label="Main navigation">
    <button type="button" class="horizontal-menu__link dropdown__trigger" aria-haspopup="true" aria-expanded="false" aria-label="View menu" data-dropdown-bound="true">
      Menu
      <span class="dropdown__trigger-caret">
        <i class="fa fa-caret-down" aria-hidden="true"></i>
      </span>
    </button>
    <ul class="dropdown__content" aria-hidden="true" aria-label="Main menu">
      <li><a class="dropdown__link" href="https://pypi.org/help/">Help</a></li>
      <li><a class="dropdown__link" href="https://pypi.org/sponsors/">Sponsors</a></li>
      <li><a class="dropdown__link" href="https://pypi.org/account/login/">Log in</a></li>
      <li><a class="dropdown__link" href="https://pypi.org/account/register/">Register</a></li>
    </ul>
  </nav>
</div>
  </div>
        </div>
      </div>
    </header>

    
    <div class="mobile-search">
      <form class="search-form search-form--fullwidth" action="https://pypi.org/search/" role="search">
        <label for="mobile-search" class="sr-only">Search PyPI</label>
        <input id="mobile-search" class="search-form__search" type="text" name="q" placeholder="Search projects" value="" autocomplete="off" autocapitalize="off" spellcheck="false">
        
        <button type="submit" class="search-form__button">
          <i class="fa fa-search" aria-hidden="true"></i>
          <span class="sr-only">Search</span>
        </button>
      </form>
    </div>
    

    <main id="content">
      
<div data-html-include="/_includes/administer-project-include/tennis"></div>

<div class="hidden" data-controller="github-repo-stats" data-github-repo-stats-github-repo-info-outlet=".github-repo-info" data-github-repo-stats-url-value="https://api.github.com/repos/bear102/tennis" data-github-repo-stats-issue-url-value="https://api.github.com/search/issues?q=repo:bear102/tennis+type:issue+state:open&amp;per_page=1">
</div>


<div class="banner">
  <div class="package-header">
    <div class="package-header__left">
      <h1 class="package-header__name">
        tennis 0.1.2
      </h1>

      
      <div data-controller="clipboard">
        <p class="package-header__pip-instructions">
          <span id="pip-command" data-clipboard-target="source">pip install tennis==0.1.2</span>
          <button type="button" class="copy-tooltip copy-tooltip-s" data-action="clipboard#copy" data-clipboard-target="tooltip" data-clipboard-tooltip-value="Copy to clipboard">
            <i class="fa fa-copy" aria-hidden="true"></i>
            <span class="sr-only">Copy PIP instructions</span>
          </button>
        </p>
      </div>
      
    </div>

    <div class="package-header__right">
    
      
      <a class="status-badge status-badge--good" href="https://pypi.org/project/tennis/">
        <span>Latest version</span>
      </a>
      
    
      <p class="package-header__date">
        Released: <time datetime="2023-05-11T02:26:45+0000" data-controller="localized-time" data-localized-time-relative="true" data-localized-time-show-time="false" title="2023-05-10 21:26:45 (-05:00)" aria-label="2023-05-10 21:26:45 (-05:00)">3 minutes ago</time>
      </p>
    </div>
  </div>
</div>

<div class="horizontal-section horizontal-section--grey horizontal-section--thin">
  <div class="site-container">
    <div class="split-layout split-layout--middle package-description">
    
      <p class="package-description__summary">A library for tracking tennis matches and scoring</p>
    
    <div data-html-include="/_includes/edit-project-button/tennis"></div>
    </div>
  </div>
</div>

<div data-controller="project-tabs" data-project-tabs-content="description">
  <div class="tabs-container">
    <div class="vertical-tabs">
      <div class="vertical-tabs__tabs">
        <div class="sidebar-section">
          <h3 class="sidebar-section__title">Navigation</h3>
          <nav aria-label="Navigation for tennis">
            <ul class="vertical-tabs__list" role="tablist">
              <li role="tab">
                <a id="description-tab" href="https://pypi.org/project/tennis/0.1.2/#description" data-project-tabs-target="tab" data-action="project-tabs#onTabClick" class="vertical-tabs__tab vertical-tabs__tab--with-icon vertical-tabs__tab--is-active" aria-selected="true" aria-label="Project description. Focus will be moved to the description.">
                  <i class="fa fa-align-left" aria-hidden="true"></i>
                  Project description
                </a>
              </li>
              <li role="tab">
                <a id="history-tab" href="https://pypi.org/project/tennis/0.1.2/#history" data-project-tabs-target="tab" data-action="project-tabs#onTabClick" class="vertical-tabs__tab vertical-tabs__tab--with-icon" aria-label="Release history. Focus will be moved to the history panel.">
                  <i class="fa fa-history" aria-hidden="true"></i>
                  Release history
                </a>
              </li>
              
              <li role="tab">
                <a id="files-tab" href="https://pypi.org/project/tennis/0.1.2/#files" data-project-tabs-target="tab" data-action="project-tabs#onTabClick" class="vertical-tabs__tab vertical-tabs__tab--with-icon" aria-label="Download files. Focus will be moved to the project files.">
                  <i class="fa fa-download" aria-hidden="true"></i>
                  Download files
                </a>
              </li>
              
            </ul>
          </nav>
        </div>
        
<div class="sidebar-section">
  <h3 class="sidebar-section__title">Project links</h3>
  <ul class="vertical-tabs__list">
    
    
    <li>
      <a class="vertical-tabs__tab vertical-tabs__tab--with-icon vertical-tabs__tab--condensed" href="https://github.com/bear102/tennis" rel="nofollow">
        


  


<i class="fas fa-home" aria-hidden="true"></i>Homepage
      </a>
    </li>
    
    
  </ul>
</div>


<div class="sidebar-section">
  <h3 class="sidebar-section__title">Statistics</h3>
  
  <div class="hidden github-repo-info" data-controller="github-repo-info">
    GitHub statistics:
    <ul class="vertical-tabs__list">
      <li>
        <a class="vertical-tabs__tab vertical-tabs__tab--with-icon vertical-tabs__tab--condensed" data-github-repo-info-target="stargazersUrl" rel="noopener">
          <i class="fa fa-star" aria-hidden="true"></i>
          <strong>Stars:</strong>
          <span data-github-repo-info-target="stargazersCount"></span>
        </a>
      </li>
      <li>
        <a class="vertical-tabs__tab vertical-tabs__tab--with-icon vertical-tabs__tab--condensed" data-github-repo-info-target="forksUrl" rel="noopener">
          <i class="fa fa-code-branch" aria-hidden="true"></i>
          <strong>Forks:</strong>
          <span data-github-repo-info-target="forksCount"></span>
        </a>
      </li>
      <li>
        <a class="vertical-tabs__tab vertical-tabs__tab--with-icon vertical-tabs__tab--condensed" data-github-repo-info-target="openIssuesUrl" rel="noopener">
          <i class="fa fa-exclamation-circle" aria-hidden="true"></i>
          <strong>Open issues:</strong>
          <span data-github-repo-info-target="openIssuesCount"></span>
        </a>
      </li>
      <li>
        <a class="vertical-tabs__tab vertical-tabs__tab--with-icon vertical-tabs__tab--condensed" data-github-repo-info-target="openPRsUrl" rel="noopener">
          <i class="fa fa-code-pull-request" aria-hidden="true"></i>
          <strong>Open PRs:</strong>
          <span data-github-repo-info-target="openPRsCount"></span>
        </a>
      </li>
    </ul>
  </div>
  
  <p>
    View statistics for this project via <a href="https://libraries.io/pypi/tennis" title="External link" target="_blank" rel="noopener">Libraries.io</a>, or by using <a href="https://packaging.python.org/guides/analyzing-pypi-package-downloads/" target="_blank" rel="noopener">our public dataset on Google BigQuery</a>
  </p>
</div>


<div class="sidebar-section">
  <h3 class="sidebar-section__title">Meta</h3>
  
  <p><strong>License:</strong> MIT License (MIT)</p>
  
  
    <p><strong>Author:</strong> bear102</p>
  
  
  
  
  <p>
    <strong>Requires:</strong> Python &gt;=3.7
  </p>
  
</div>


<div class="sidebar-section">
  
  
    <h3 class="sidebar-section__title">Maintainers</h3>
    
      
      <span class="sidebar-section__maintainer">
        <a href="https://pypi.org/user/bear102/" aria-label="bear102">
          <span class="sidebar-section__user-gravatar">
            <img src="./rm_files/68747470733a2f2f7365637572652e67726176617461722e636f6d2f6176617461722f34343565303366666433613432366538636662393566343136386266393034393f73697a653d3530" height="50" width="50" alt="Avatar for bear102 from gravatar.com" title="Avatar for bear102 from gravatar.com">
          </span>
          <span class="sidebar-section__user-gravatar-text">
            bear102
          </span>
        </a>
      </span>
    
  
</div>


<div class="sidebar-section">
  <h3 class="sidebar-section__title">Classifiers</h3>
  <ul class="sidebar-section__classifiers">
    
    <li>
      <strong>License</strong>
      <ul>
        
        <li>
          <a href="https://pypi.org/search/?c=License+%3A%3A+OSI+Approved+%3A%3A+MIT+License">
            OSI Approved :: MIT License
          </a>
        </li>
        
      </ul>
    </li>
    
    <li>
      <strong>Operating System</strong>
      <ul>
        
        <li>
          <a href="https://pypi.org/search/?c=Operating+System+%3A%3A+OS+Independent">
            OS Independent
          </a>
        </li>
        
      </ul>
    </li>
    
    <li>
      <strong>Programming Language</strong>
      <ul>
        
        <li>
          <a href="https://pypi.org/search/?c=Programming+Language+%3A%3A+Python+%3A%3A+3">
            Python :: 3
          </a>
        </li>
        
      </ul>
    </li>
    
  </ul>
</div>

        
        
<div class="sidebar-section loaded" data-ea-publisher="psf" data-ea-type="psf" data-ea-keywords="pypi-sidebar"><div class="ethical-sidebar"><div class="ethical-content"><a href="https://server.ethicalads.io/proxy/click/3341/11bf76e9-3773-425a-83b0-ce4a5be156dd/" rel="nofollow noopener" target="_blank" class="ethical-image-link"><img src="./rm_files/Ansys_Logo_WhiteBackground_PNG_09XFnlV.png" alt="Sponsored: Python Software Foundation"></a><div class="ethical-text">Ansys is a Maintaining sponsor of the Python Software Foundation.</div></div><div class="ethical-callout"><small><em><a href="https://www.python.org/psf/sponsorship/?ref=ethicalads-placement">PSF Sponsor</a><span> · </span><a href="https://www.ethicalads.io/sponsorship-platform/?ref=psf">Served ethically</a></em></small></div></div><img src="./rm_files/saved_resource(1)" class="ea-pixel"><img src="./rm_files/saved_resource(2)" class="ea-pixel"></div>


      </div>
      <div class="vertical-tabs__panel">
        <!-- mobile menu -->
        <nav aria-label="Navigation for tennis">
          <ul class="vertical-tabs__list" role="tablist">
            <li role="tab">
              <a id="mobile-description-tab" href="https://pypi.org/project/tennis/0.1.2/#description" data-project-tabs-target="mobileTab" data-action="project-tabs#onTabClick" class="vertical-tabs__tab vertical-tabs__tab--with-icon vertical-tabs__tab--mobile vertical-tabs__tab--no-top-border vertical-tabs__tab--is-active" aria-selected="true" aria-label="Project description. Focus will be moved to the description.">
                <i class="fa fa-align-left" aria-hidden="true"></i>
                Project description
              </a>
            </li>
            <li role="tab">
              <a id="mobile-data-tab" href="https://pypi.org/project/tennis/0.1.2/#data" data-project-tabs-target="mobileTab" data-action="project-tabs#onTabClick" class="vertical-tabs__tab vertical-tabs__tab--with-icon vertical-tabs__tab--mobile" aria-label="Project details. Focus will be moved to the project details.">
                <i class="fa fa-info-circle" aria-hidden="true"></i>
                Project details
              </a>
            </li>
            <li role="tab">
              <a id="mobile-history-tab" href="https://pypi.org/project/tennis/0.1.2/#history" data-project-tabs-target="mobileTab" data-action="project-tabs#onTabClick" class="vertical-tabs__tab vertical-tabs__tab--with-icon vertical-tabs__tab--mobile" aria-label="Release history. Focus will be moved to the history panel.">
              <i class="fa fa-history" aria-hidden="true"></i>
              Release history
            </a>
            </li>
            
            <li role="tab">
              <a id="mobile-files-tab" href="https://pypi.org/project/tennis/0.1.2/#files" data-project-tabs-target="mobileTab" data-action="project-tabs#onTabClick" class="vertical-tabs__tab vertical-tabs__tab--with-icon vertical-tabs__tab--mobile" aria-label="Download files. Focus will be moved to the project files.">
                <i class="fa fa-download" aria-hidden="true"></i>
                Download files
              </a>
            </li>
            
          </ul>
        </nav>

        
        <div id="description" data-project-tabs-target="content" class="vertical-tabs__content" role="tabpanel" aria-labelledby="description-tab mobile-description-tab" tabindex="-1" style="display: block;">
          <h2 class="page-title">Project description</h2>
          
          <div class="project-description">
            <h1>Tennis Library</h1>
<p><a href="https://github.com/bear102" rel="nofollow"><img src="./rm_files/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769744875622d626561723130322d2532333132313030452e7376673f7374796c653d666c6174266c6f676f3d676974687562" alt="GitHub"></a>
<img src="./rm_files/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d332e37253230253743253230332e38253230253743253230332e392d626c7565" alt="Python">
<a href="https://opensource.org/licenses/MIT" rel="nofollow"><img src="./rm_files/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d4d49542d626c75652e737667" alt="License"></a></p>
<p>The Tennis library is a Python package that provides functionalities for simulating tennis matches and tiebreakers. It offers easy-to-use methods to simulate and track scores, tiebreakers, and various statistics. The tennis library is perfect for tracking real time data input.</p>
<br>
<h2><strong>Table Of Contents</strong></h2>
<ul>
<li><a href="https://pypi.org/project/tennis/0.1.2/#tennis-library" rel="nofollow">Tennis Library</a>
<ul>
<li><a href="https://pypi.org/project/tennis/0.1.2/#table-of-contents" rel="nofollow"><strong>Table Of Contents</strong></a></li>
<li><a href="https://pypi.org/project/tennis/0.1.2/#features" rel="nofollow">Features</a>
<ul>
<li><a href="https://pypi.org/project/tennis/0.1.2/#1-match-simulation" rel="nofollow">1. Match Simulation</a></li>
<li><a href="https://pypi.org/project/tennis/0.1.2/#2-tiebreaker" rel="nofollow">2. Tiebreaker</a></li>
<li><a href="https://pypi.org/project/tennis/0.1.2/#tracking-stats" rel="nofollow">Tracking Stats</a></li>
</ul>
</li>
<li><a href="https://pypi.org/project/tennis/0.1.2/#usage" rel="nofollow">Usage</a>
<ul>
<li><a href="https://pypi.org/project/tennis/0.1.2/#quick-start" rel="nofollow">Quick Start</a></li>
<li><a href="https://pypi.org/project/tennis/0.1.2/#match-methods" rel="nofollow">Match Methods</a>
<ul>
<li><a href="https://pypi.org/project/tennis/0.1.2/#tennismatch-self-player1str-player2str-matchformatdictnone" rel="nofollow">TennisMatch (self, player1:str, player2:str, matchFormat:dict=None)</a></li>
<li><a href="https://pypi.org/project/tennis/0.1.2/#backup_match-" rel="nofollow"><code>backup_match</code> ()</a></li>
<li><a href="https://pypi.org/project/tennis/0.1.2/#load_backup-self-backup_data" rel="nofollow"><code>load_backup</code> (self, backup_data)</a></li>
<li><a href="https://pypi.org/project/tennis/0.1.2/#win_point-self-playerstr-how_won" rel="nofollow"><strong><code>win_point</code></strong> (self, player:str, how_won=[])</a></li>
<li><a href="https://pypi.org/project/tennis/0.1.2/#serve_fault-self-playerstr" rel="nofollow"><code>serve_fault</code> (self, player:str)</a></li>
<li><a href="https://pypi.org/project/tennis/0.1.2/#win_game-self-playerstr" rel="nofollow"><code>win_game</code> (self, player:str)</a></li>
<li><a href="https://pypi.org/project/tennis/0.1.2/#win_set-self-playerstr" rel="nofollow"><code>win_set</code> (self, player:str)</a></li>
<li><a href="https://pypi.org/project/tennis/0.1.2/#get_all_info-self" rel="nofollow"><code>get_all_info</code> (self)</a></li>
<li><a href="https://pypi.org/project/tennis/0.1.2/#get_scoreboard-self-playerstr" rel="nofollow"><code>get_scoreboard</code> (self, player:str)</a></li>
<li><a href="https://pypi.org/project/tennis/0.1.2/#match_stats-self-playerstr" rel="nofollow"><code>match_stats</code> (self, player:str)</a></li>
</ul>
</li>
<li><a href="https://pypi.org/project/tennis/0.1.2/#tiebreak-methods" rel="nofollow">Tiebreak Methods</a>
<ul>
<li><a href="https://pypi.org/project/tennis/0.1.2/#tiebreak-self-player1str-player2str-matchformatdictnone" rel="nofollow">Tiebreak (self, player1:str, player2:str, matchFormat:dict=None)</a></li>
<li><a href="https://pypi.org/project/tennis/0.1.2/#backup_tiebreak-" rel="nofollow">backup_tiebreak ()</a></li>
<li><a href="https://pypi.org/project/tennis/0.1.2/#load_backup-self-backup_data-1" rel="nofollow">load_backup (self, backup_data)</a></li>
<li><a href="https://pypi.org/project/tennis/0.1.2/#win_point-self-playerstr-how_won-1" rel="nofollow"><code>win_point</code> (self, player:str, how_won=[])</a></li>
<li><a href="https://pypi.org/project/tennis/0.1.2/#tiebreak_stats-self-playerstr" rel="nofollow"><code>tiebreak_stats</code> (self, player:str)</a></li>
<li><a href="https://pypi.org/project/tennis/0.1.2/#get_scoreboard-self-playerstr-1" rel="nofollow"><code>get_scoreboard</code> (self, player:str)</a></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<h2><a href="https://pypi.org/project/tennis/0.1.2/#features" rel="nofollow">Features</a></h2>
<p>The Tennis library offers the following main features:
<br></p>
<h3><a href="https://pypi.org/project/tennis/0.1.2/#1-match-simulation" rel="nofollow">1. Match Simulation</a></h3>
<p>The match simulation feature allows you to simulate a full tennis match between two players. It will automatically keep track of match stats and comply with complicated rules like tiebreakers, AD, and serving
<br></p>
<h3><a href="https://pypi.org/project/tennis/0.1.2/#2-tiebreaker" rel="nofollow">2. Tiebreaker</a></h3>
<p>The tiebreaker feature enables you to simulate a tiebreakerIt provides an easy-to-use interface for conducting tiebreakers, scoring points, and tracking statistics.
<br></p>
<h3><a href="https://pypi.org/project/tennis/0.1.2/#tracking-stats" rel="nofollow">Tracking Stats</a></h3>
<p>Both the match simulation and tiebreaker features include built-in mechanisms for tracking various statistics. These statistics include:</p>
<ul>
<li>Aces</li>
<li>Double faults</li>
<li>First serve percentage</li>
<li>First serve points won</li>
<li>Second serve percentage</li>
<li>Second serve points won</li>
<li>Serve games won</li>
<li>Return games won</li>
<li>Winners</li>
<li>Unforced errors</li>
<li>Points won by volley</li>
<li>Points won by dropshot</li>
<li>Points won by overhead</li>
</ul>
<p>These statistics help analyze player performance and provide insights into the gameplay.</p>
<br>
<hr>
<br>
<h2><a href="https://pypi.org/project/tennis/0.1.2/#usage" rel="nofollow">Usage</a></h2>
<p>To use the Tennis library, follow these steps:</p>
<ol>
<li>Install the library by running <br> <code>pip install tennis</code>.
<br><br></li>
<li>import libraries<br></li>
</ol>
<pre lang="python3"><span class="kn">from</span> <span class="nn">tennis</span> <span class="kn">import</span> <span class="n">match</span>

<span class="kn">from</span> <span class="nn">tennis</span> <span class="kn">import</span> <span class="n">tiebreak</span>
</pre>
<h3><a href="https://pypi.org/project/tennis/0.1.2/#quick-start" rel="nofollow">Quick Start</a></h3>
<br>
Here's an example of how to simulate a tennis match using the Tennis library:
<pre lang="python3"><span class="kn">from</span> <span class="nn">tennis</span> <span class="kn">import</span> <span class="n">match</span>

<span class="c1"># create a new match instance</span>
<span class="n">a</span> <span class="o">=</span> <span class="n">match</span><span class="o">.</span><span class="n">TennisMatch</span><span class="p">(</span><span class="s2">"a"</span><span class="p">,</span><span class="s2">"b"</span><span class="p">,{</span><span class="s2">"num_games_to_win"</span><span class="p">:</span><span class="mi">6</span><span class="p">,</span> <span class="s2">"best_of_num_sets"</span><span class="p">:</span><span class="mi">3</span><span class="p">,</span> <span class="s2">"whos_serve"</span><span class="p">:</span><span class="s2">"a"</span><span class="p">,</span> <span class="s2">"with_AD"</span><span class="p">:</span><span class="kc">True</span><span class="p">})</span>

<span class="c1"># call win_point() player "a" won the point by an "overhead, opponent unforced error, and a dropshot"</span>
<span class="n">a</span><span class="o">.</span><span class="n">win_point</span><span class="p">(</span><span class="s2">"a"</span><span class="p">,</span> <span class="p">[</span><span class="s2">"overhead"</span><span class="p">])</span>
<span class="n">a</span><span class="o">.</span><span class="n">win_point</span><span class="p">(</span><span class="s2">"a"</span><span class="p">,[</span><span class="s1">'unforced_errors'</span><span class="p">])</span>
<span class="n">a</span><span class="o">.</span><span class="n">win_point</span><span class="p">(</span><span class="s2">"a"</span><span class="p">,</span> <span class="p">[</span><span class="s2">"win_by_dropshot"</span><span class="p">])</span>

<span class="c1"># gets a string representation of the scoreboard. Player "a" score will be displayed on top</span>
<span class="nb">print</span><span class="p">(</span><span class="n">a</span><span class="o">.</span><span class="n">get_scoreboard</span><span class="p">(</span><span class="s2">"a"</span><span class="p">))</span>

<span class="c1"># gets a string representation of the stats. Player "a" will be displayed on the left</span>
<span class="nb">print</span><span class="p">(</span><span class="n">a</span><span class="o">.</span><span class="n">print_stats</span><span class="p">(</span><span class="s2">"a"</span><span class="p">))</span>
</pre>
<p>output:</p>
<pre><code>╔═════════════════════════════════════╗
              Match Score

    M  S  G  T
    0  0  40   *                a
    0  0  0                    b

╚═════════════════════════════════════╝


════════════════════════════════════════

a vs b
100 - First Serve Percentage - NA

3 - First Serve Points Won - 0

NA - Second Serve Percentage - NA

0 - Second Serve Points Won - 0

0 - Serve Games Won - 0

0 - Return Games Won - 0

3 - Total Points Won - 0

0 - Aces - 0

0 - Double Faults - 0

0 - Winners - 0

0 - Unforced Errors - 1

0 - Points Won By Volley - 0

1 - Points Won By Dropshot - 0

0 - Points Won By Overhead - 0



════════════════════════════════════════
</code></pre>
<br>
<hr>
<br>
<p>Here's an example of how to simulate a tennis tiebreak using the Tennis library:</p>
<pre lang="python3"><span class="kn">from</span> <span class="nn">tennis</span> <span class="kn">import</span> <span class="n">tiebreak</span>

<span class="c1">#create a new tiebreak instance</span>
<span class="n">tb</span> <span class="o">=</span> <span class="n">tiebreak</span><span class="o">.</span><span class="n">tiebreak</span><span class="p">(</span><span class="s2">"a"</span><span class="p">,</span><span class="s2">"b"</span><span class="p">,{</span><span class="s2">"first_to_num_points"</span><span class="p">:</span><span class="mi">7</span><span class="p">,</span> <span class="s2">"win_by"</span><span class="p">:</span><span class="mi">2</span><span class="p">,</span> <span class="s2">"whos_serve"</span><span class="p">:</span><span class="s2">"a"</span><span class="p">})</span>

<span class="c1">#player "a" wins the point</span>
<span class="n">tb</span><span class="o">.</span><span class="n">win_point</span><span class="p">(</span><span class="s2">"a"</span><span class="p">)</span>

<span class="c1">#player "b" misses a first serve</span>
<span class="n">tb</span><span class="o">.</span><span class="n">serve_fault</span><span class="p">(</span><span class="s2">"b"</span><span class="p">)</span>

<span class="c1">#returns a string representation of the scoreboard</span>
<span class="nb">print</span><span class="p">(</span><span class="n">tb</span><span class="o">.</span><span class="n">get_scoreboard</span><span class="p">(</span><span class="s2">"a"</span><span class="p">))</span>
</pre>
<p>output:</p>
<pre><code>╔═════════════════════════════════════╗
            Tiebreak Score

     T
     1                   a
     0  *                b

╚═════════════════════════════════════╝



════════════════════════════════════════

a vs b
100 - First Serve Percentage - NA

3 - First Serve Points Won - 0

NA - Second Serve Percentage - NA

0 - Second Serve Points Won - 0

0 - Serve Games Won - 0

0 - Return Games Won - 0

3 - Total Points Won - 0

0 - Aces - 0

0 - Double Faults - 0

0 - Winners - 0

0 - Unforced Errors - 1

0 - Points Won By Volley - 0

1 - Points Won By Dropshot - 0

0 - Points Won By Overhead - 0



════════════════════════════════════════
</code></pre>
<p><br><br><br></p>
<h3></h3><h1><a href="https://pypi.org/project/tennis/0.1.2/#match-methods" rel="nofollow">Match Methods</a></h1>
<h4><a href="https://pypi.org/project/tennis/0.1.2/#tennismatch" rel="nofollow">TennisMatch</a> (self, player1:str, player2:str, matchFormat:dict=None)</h4>
<p>Creates a new instance of a tennis match.</p>
<p><strong>Parameters</strong></p>
<ul>
<li>player1 (str): The name of player 1.</li>
<li>player2 (str): The name of player 2.</li>
<li>matchFormat (dict): A dictionary of match settings.</li>
</ul>
<p><strong>Example</strong></p>
<pre lang="python3"><span class="n">match</span> <span class="o">=</span> <span class="n">TennisMatch</span><span class="p">(</span><span class="s2">"a"</span><span class="p">,</span> <span class="s2">"b"</span><span class="p">,{</span><span class="s2">"num_games_to_win"</span><span class="p">:</span><span class="mi">2</span><span class="p">,</span> <span class="s2">"best_of_num_sets"</span><span class="p">:</span><span class="mi">3</span><span class="p">,</span> <span class="s2">"whos_serve"</span><span class="p">:</span><span class="s2">"a"</span><span class="p">,</span> <span class="s2">"with_AD"</span><span class="p">:</span><span class="kc">True</span><span class="p">})</span>
</pre>
<br>
<hr>
<br>
<h4><a href="https://pypi.org/project/tennis/0.1.2/#backup_match" rel="nofollow"><code>backup_match</code></a> ()</h4>
<p>Creates a backup for the current tennis match instance</p>
<h4><a href="https://pypi.org/project/tennis/0.1.2/#load_backup" rel="nofollow"><code>load_backup</code></a> (self, backup_data)</h4>
<p>Loads a backup into a new match</p>
<p><strong>Parameters</strong></p>
<ul>
<li>backup_data (dict): The backup data created by the backup_match method</li>
</ul>
<p><strong>Example</strong></p>
<pre lang="python3"><span class="n">backup_data</span> <span class="o">=</span> <span class="n">match</span><span class="o">.</span><span class="n">backup_match</span><span class="p">()</span>

<span class="n">new_match</span> <span class="o">=</span> <span class="n">TennisMatch</span><span class="p">(</span><span class="s2">"dawda"</span><span class="p">,</span><span class="s2">"nnnn"</span><span class="p">,{</span><span class="s2">"num_games_to_win"</span><span class="p">:</span><span class="mi">2</span><span class="p">,</span> <span class="s2">"best_of_num_sets"</span><span class="p">:</span><span class="mi">3</span><span class="p">,</span> <span class="s2">"whos_serve"</span><span class="p">:</span><span class="s2">"a"</span><span class="p">,</span> <span class="s2">"with_AD"</span><span class="p">:</span><span class="kc">True</span><span class="p">})</span>

<span class="n">new_match</span> <span class="o">=</span> <span class="n">new_match</span><span class="o">.</span><span class="n">load_backup</span><span class="p">(</span><span class="n">backup_data</span><span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="n">new_match</span><span class="o">.</span><span class="n">match_stats</span><span class="p">(</span><span class="s2">"a"</span><span class="p">))</span>
</pre>
<br>
<hr>
<br>
<h4><strong><a href="https://pypi.org/project/tennis/0.1.2/#win_point" rel="nofollow"><code>win_point</code></a></strong> (self, player:str, how_won=[])</h4>
<p>method that handles a player winning or loosing a point. Do not call this method if it is a double fault. Instead, call the <a href="https://pypi.org/project/tennis/0.1.2/#serve_fault-self-playerstr" rel="nofollow"><code>serve_fault</code> (self, player:str)</a> method</p>
<p><strong>Parameters</strong></p>
<ul>
<li>player (str): The name of the player who won the point.</li>
<li>how_won (Array): How the point was won (more than 1 in a method call is ok, just append them to the end of the list like ['winner','win_by_volley'])
<ul>
<li><code>Ace</code>: player A wins by by acing player b (Player A's serves the ball in and player B does not even touch the ball)</li>
<li><code>winner</code>: player A wins the point by hitting a winner. (The opponent doesnt touch the ball at all)</li>
<li><code>unforced_error</code>: player A wins the point because player B made an unforced error (An error that was not caused by player A. For example player B got an easy ball and missed it)</li>
<li><code>win_by_volley</code>: player A wins the point on a volley (Hitting the ball when it hasnt bounced right out of the air)</li>
<li><code>win_by_dropshot</code>: player A wins the point with a dropshot (player A lightly hits a short ball close to the net)</li>
<li><code>win_by_overhead</code>: player A wins the point via an overhead (player A "smashes" the ball right out of the air)</li>
</ul>
</li>
</ul>
<p><strong>Example</strong></p>
<pre lang="python3"><span class="k">match</span><span class="o">.</span><span class="n">win_point</span><span class="p">(</span><span class="s2">"a"</span><span class="p">)</span>
<span class="k">match</span><span class="o">.</span><span class="n">win_point</span><span class="p">(</span><span class="s2">"b"</span><span class="p">,</span> <span class="p">[</span><span class="s1">'win_by_volley'</span><span class="p">])</span>
<span class="k">match</span><span class="o">.</span><span class="n">win_point</span><span class="p">(</span><span class="s2">"b"</span><span class="p">,</span> <span class="p">[</span><span class="s1">'win_by_volley'</span><span class="p">,</span><span class="s1">'winner'</span><span class="p">])</span>
</pre>
<br>
<hr>
<br>
<h4><a href="https://pypi.org/project/tennis/0.1.2/#serve_fault" rel="nofollow"><code>serve_fault</code></a> (self, player:str)</h4>
<p>method to call when a server misses a first or second serve</p>
<p><strong>Parameters</strong></p>
<ul>
<li>player (str): The name of the player who missed the serve</li>
</ul>
<p><strong>Example</strong></p>
<pre lang="python3"><span class="c1">#double fault</span>
<span class="k">match</span><span class="o">.</span><span class="n">serve_fault</span><span class="p">(</span><span class="s2">"a"</span><span class="p">)</span>
<span class="k">match</span><span class="o">.</span><span class="n">serve_fault</span><span class="p">(</span><span class="s2">"a"</span><span class="p">)</span>

<span class="c1">#missed first serve and made second serve</span>
<span class="k">match</span><span class="o">.</span><span class="n">serve_fault</span><span class="p">(</span><span class="s2">"a"</span><span class="p">)</span>
<span class="k">match</span><span class="o">.</span><span class="n">win_point</span><span class="p">(</span><span class="s2">"a"</span><span class="p">)</span>
</pre>
<br>
<hr>
<br>
<h4><a href="https://pypi.org/project/tennis/0.1.2/#win_game" rel="nofollow"><code>win_game</code></a> (self, player:str)</h4>
<p>A method that will win the game for a player. This method is intended for development and testing. The statistics for the match will be off.</p>
<p><strong>Parameters</strong></p>
<ul>
<li>player (str): the player that will win the game</li>
</ul>
<p><strong>Example</strong></p>
<pre lang="python3"><span class="k">match</span><span class="o">.</span><span class="n">win_game</span><span class="p">(</span><span class="s2">"a"</span><span class="p">)</span>
</pre>
<br>
<hr>
<br>
<h4><a href="https://pypi.org/project/tennis/0.1.2/#win_set" rel="nofollow"><code>win_set</code></a> (self, player:str)</h4>
<p>A method that will win the set for a player. This method is intended for development and testing. The statistics for the match will be off.</p>
<p><strong>Parameters</strong></p>
<ul>
<li>player (str): the player that will win the set</li>
</ul>
<p><strong>Example</strong></p>
<pre lang="python3"><span class="k">match</span><span class="o">.</span><span class="n">win_set</span><span class="p">(</span><span class="s2">"a"</span><span class="p">)</span>
</pre>
<br>
<hr>
<br>
<h4><a href="https://pypi.org/project/tennis/0.1.2/#get_all_info" rel="nofollow"><code>get_all_info</code></a> (self)</h4>
<p>A method that will return all the info about the match in a dictionary format</p>
<pre lang="python3"><span class="k">return</span> <span class="p">{</span><span class="s2">"winner"</span><span class="p">:</span><span class="bp">self</span><span class="o">.</span><span class="n">winner</span><span class="p">,</span> <span class="s2">"game_history"</span><span class="p">:</span><span class="bp">self</span><span class="o">.</span><span class="n">gameHistory</span><span class="p">,</span> <span class="s2">"set_history"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">setHistory</span><span class="p">,</span> <span class="s2">"set_tiebreak_history"</span><span class="p">:</span><span class="bp">self</span><span class="o">.</span><span class="n">setTieBreakScoresHistory</span><span class="p">,</span> <span class="s2">"match_tiebreak_history"</span><span class="p">:</span><span class="bp">self</span><span class="o">.</span><span class="n">matchTieBreakScore</span><span class="p">,</span><span class="s2">"match_format"</span><span class="p">:</span><span class="bp">self</span><span class="o">.</span><span class="n">matchFormat</span><span class="p">,</span><span class="s2">"match_stats"</span><span class="p">:</span><span class="bp">self</span><span class="o">.</span><span class="n">matchStats</span><span class="p">}</span>
</pre>
<p><strong>example output</strong></p>
<pre lang="python3"><span class="p">{</span><span class="s1">'winner'</span><span class="p">:</span> <span class="s1">''</span><span class="p">,</span> <span class="s1">'game_history'</span><span class="p">:</span> <span class="p">[{</span><span class="s1">'a'</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span> <span class="s1">'b'</span><span class="p">:</span> <span class="mi">0</span><span class="p">}],</span> <span class="s1">'set_history'</span><span class="p">:</span> <span class="p">[{</span><span class="s1">'a'</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span> <span class="s1">'b'</span><span class="p">:</span> <span class="mi">0</span><span class="p">},</span> <span class="p">{</span><span class="s1">'a'</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span> <span class="s1">'b'</span><span class="p">:</span> <span class="mi">0</span><span class="p">}],</span> <span class="s1">'set_tiebreak_history'</span><span class="p">:</span> <span class="p">[],</span> <span class="s1">'match_tiebreak_history'</span><span class="p">:</span> <span class="p">{</span><span class="s1">'a'</span><span class="p">:</span> <span class="mi">1</span><span class="p">,</span> <span class="s1">'b'</span><span class="p">:</span> <span class="mi">4</span><span class="p">},</span> <span class="s1">'match_format'</span><span class="p">:</span> <span class="p">{</span><span class="s1">'num_games_to_win'</span><span class="p">:</span> <span class="mi">2</span><span class="p">,</span> <span class="s1">'best_of_num_sets'</span><span class="p">:</span> <span class="mi">3</span><span class="p">,</span> <span class="s1">'whos_serve'</span><span class="p">:</span> <span class="s1">'b'</span><span class="p">,</span> <span class="s1">'with_AD'</span><span class="p">:</span> <span class="kc">True</span><span class="p">},</span> <span class="s1">'match_stats'</span><span class="p">:</span> <span class="p">{</span><span class="s1">'Aces'</span><span class="p">:</span> <span class="p">{</span><span class="s1">'a'</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span> <span class="s1">'b'</span><span class="p">:</span> <span class="mi">0</span><span class="p">},</span> <span class="s1">'Double_fault'</span><span class="p">:</span> <span class="p">{</span><span class="s1">'a'</span><span class="p">:</span> <span class="mi">2</span><span class="p">,</span> <span class="s1">'b'</span><span class="p">:</span> <span class="mi">1</span><span class="p">},</span> <span class="s1">'first_serve_percent'</span><span class="p">:</span> <span class="p">{</span><span class="s1">'a'</span><span class="p">:</span> <span class="mi">33</span><span class="p">,</span> <span class="s1">'b'</span><span class="p">:</span> <span class="mf">33.33</span><span class="p">},</span> <span class="s1">'first_serve_points_won'</span><span class="p">:</span> <span class="p">{</span><span class="s1">'a'</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span> <span class="s1">'b'</span><span class="p">:</span> <span class="mi">1</span><span class="p">},</span> <span class="s1">'second_serve_percent'</span><span class="p">:</span> <span class="p">{</span><span class="s1">'a'</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span> <span class="s1">'b'</span><span class="p">:</span> <span class="mi">0</span><span class="p">},</span> <span class="s1">'second_serve_points_won'</span><span class="p">:</span> <span class="p">{</span><span class="s1">'a'</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span> <span class="s1">'b'</span><span class="p">:</span> <span class="mi">0</span><span class="p">},</span> <span class="s1">'winners'</span><span class="p">:</span> <span class="p">{</span><span class="s1">'a'</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span> <span class="s1">'b'</span><span class="p">:</span> <span class="mi">0</span><span class="p">},</span> <span class="s1">'unforced_errors'</span><span class="p">:</span> <span class="p">{</span><span class="s1">'a'</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span> <span class="s1">'b'</span><span class="p">:</span> <span class="mi">0</span><span class="p">},</span> <span class="s1">'win_by_volley'</span><span class="p">:</span> <span class="p">{</span><span class="s1">'a'</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span> <span class="s1">'b'</span><span class="p">:</span> <span class="mi">0</span><span class="p">},</span> <span class="s1">'win_by_dropshot'</span><span class="p">:</span> <span class="p">{</span><span class="s1">'a'</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span> <span class="s1">'b'</span><span class="p">:</span> <span class="mi">0</span><span class="p">},</span> <span class="s1">'win_by_overhead'</span><span class="p">:</span> <span class="p">{</span><span class="s1">'a'</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span> <span class="s1">'b'</span><span class="p">:</span> <span class="mi">0</span><span class="p">},</span> <span class="s1">'serve_games_won'</span><span class="p">:</span> <span class="p">{</span><span class="s1">'a'</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span> <span class="s1">'b'</span><span class="p">:</span> <span class="mi">0</span><span class="p">},</span> <span class="s1">'return_games_won'</span><span class="p">:</span> <span class="p">{</span><span class="s1">'a'</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span> <span class="s1">'b'</span><span class="p">:</span> <span class="mi">0</span><span class="p">}}}</span>
</pre>
<br>
<hr>
<br>
<h4><a href="https://pypi.org/project/tennis/0.1.2/#get_scoreboard" rel="nofollow"><code>get_scoreboard</code></a> (self, player:str)</h4>
<p>A method that will return a string representation of the current scoreboard.</p>
<p><strong>Parameters</strong></p>
<ul>
<li>player (str): the player whos name and score will appear on the top half of the scoreboard</li>
</ul>
<p><strong>Example Output</strong></p>
<pre lang="python3"><span class="err">╔═════════════════════════════════════╗</span>
              <span class="n">Match</span> <span class="n">Score</span>

    <span class="n">M</span>  <span class="n">S</span>  <span class="n">G</span>  <span class="n">T</span>
    <span class="mi">1</span>  <span class="mi">0</span>  <span class="mi">0</span>  <span class="mi">1</span>                  <span class="n">a</span>
    <span class="mi">1</span>  <span class="mi">0</span>  <span class="mi">0</span>  <span class="mi">4</span> <span class="o">*</span>                <span class="n">b</span>

<span class="err">╚═════════════════════════════════════╝</span>
</pre>
<br>
<hr>
<br>
<h4><a href="https://pypi.org/project/tennis/0.1.2/#match_stats" rel="nofollow"><code>match_stats</code></a> (self, player:str)</h4>
<p>A method that will return the statistics about the match in a string format</p>
<p><strong>Parameters</strong></p>
<ul>
<li>player (str): the player who will appear on the left side of the stats</li>
</ul>
<p><strong>Example Output</strong></p>
<pre lang="python3"><span class="err">════════════════════════════════════════</span>

<span class="n">a</span> <span class="n">vs</span> <span class="n">b</span>
<span class="mi">33</span> <span class="o">-</span> <span class="n">First</span> <span class="n">Serve</span> <span class="n">Percentage</span> <span class="o">-</span> <span class="mf">33.33</span>

<span class="mi">0</span> <span class="o">-</span> <span class="n">First</span> <span class="n">Serve</span> <span class="n">Points</span> <span class="n">Won</span> <span class="o">-</span> <span class="mi">1</span>

<span class="mi">0</span> <span class="o">-</span> <span class="n">Second</span> <span class="n">Serve</span> <span class="n">Percentage</span> <span class="o">-</span> <span class="mi">0</span>

<span class="mi">0</span> <span class="o">-</span> <span class="n">Second</span> <span class="n">Serve</span> <span class="n">Points</span> <span class="n">Won</span> <span class="o">-</span> <span class="mi">0</span>

<span class="mi">0</span> <span class="o">-</span> <span class="n">Serve</span> <span class="n">Games</span> <span class="n">Won</span> <span class="o">-</span> <span class="mi">0</span>

<span class="mi">0</span> <span class="o">-</span> <span class="n">Return</span> <span class="n">Games</span> <span class="n">Won</span> <span class="o">-</span> <span class="mi">0</span>

<span class="mi">1</span> <span class="o">-</span> <span class="n">Total</span> <span class="n">Points</span> <span class="n">Won</span> <span class="o">-</span> <span class="mi">4</span>

<span class="mi">0</span> <span class="o">-</span> <span class="n">Aces</span> <span class="o">-</span> <span class="mi">0</span>

<span class="mi">2</span> <span class="o">-</span> <span class="n">Double</span> <span class="n">Faults</span> <span class="o">-</span> <span class="mi">1</span>

<span class="mi">0</span> <span class="o">-</span> <span class="n">Winners</span> <span class="o">-</span> <span class="mi">0</span>

<span class="mi">0</span> <span class="o">-</span> <span class="n">Unforced</span> <span class="n">Errors</span> <span class="o">-</span> <span class="mi">0</span>

<span class="mi">0</span> <span class="o">-</span> <span class="n">Points</span> <span class="n">Won</span> <span class="n">By</span> <span class="n">Volley</span> <span class="o">-</span> <span class="mi">0</span>

<span class="mi">0</span> <span class="o">-</span> <span class="n">Points</span> <span class="n">Won</span> <span class="n">By</span> <span class="n">Dropshot</span> <span class="o">-</span> <span class="mi">0</span>

<span class="mi">0</span> <span class="o">-</span> <span class="n">Points</span> <span class="n">Won</span> <span class="n">By</span> <span class="n">Overhead</span> <span class="o">-</span> <span class="mi">0</span>



<span class="err">════════════════════════════════════════</span>
</pre>
<p><br><br></p>
<h3></h3><h1><a href="https://pypi.org/project/tennis/0.1.2/#tiebreak-methods" rel="nofollow">Tiebreak Methods</a></h1>
<h4><a href="https://pypi.org/project/tennis/0.1.2/#tiebreak" rel="nofollow">Tiebreak</a> (self, player1:str, player2:str, matchFormat:dict=None)</h4>
<p>Creates a new instance of a tiebreak.</p>
<p><strong>Parameters</strong></p>
<ul>
<li>player1 (str): the name of the first player</li>
<li>player2 (str): the name of the second player</li>
<li>matchFormat (dict): A dictionary of match settings.</li>
</ul>
<p><strong>Example</strong></p>
<pre lang="python3"><span class="n">match</span> <span class="o">=</span> <span class="n">tiebreak</span><span class="p">(</span><span class="s2">"a"</span><span class="p">,</span><span class="s2">"b"</span><span class="p">,{</span><span class="s2">"first_to_num_points"</span><span class="p">:</span><span class="mi">7</span><span class="p">,</span> <span class="s2">"win_by"</span><span class="p">:</span><span class="mi">2</span><span class="p">,</span> <span class="s2">"whos_serve"</span><span class="p">:</span><span class="s2">"a"</span><span class="p">})</span>
</pre>
<br>
<hr>
<br>
<h4><a href="https://pypi.org/project/tennis/0.1.2/#backup_tiebreak" rel="nofollow">backup_tiebreak</a> ()</h4>
<p>A method to backup tiebreak data</p>
<p><strong>Example</strong></p>
<pre lang="python3"><span class="n">match</span> <span class="o">=</span> <span class="n">tiebreak</span><span class="p">(</span><span class="s2">"a"</span><span class="p">,</span><span class="s2">"b"</span><span class="p">,{</span><span class="s2">"first_to_num_points"</span><span class="p">:</span><span class="mi">7</span><span class="p">,</span> <span class="s2">"win_by"</span><span class="p">:</span><span class="mi">2</span><span class="p">,</span> <span class="s2">"whos_serve"</span><span class="p">:</span><span class="s2">"a"</span><span class="p">})</span>
<span class="n">backup_data</span> <span class="o">=</span> <span class="n">match</span><span class="o">.</span><span class="n">backup_tiebreak</span><span class="p">()</span>
</pre>
<h4><a href="https://pypi.org/project/tennis/0.1.2/#load_backup" rel="nofollow">load_backup</a> (self, backup_data)</h4>
<p>A method to load backup data from another tiebreak object</p>
<p><strong>Parameters</strong></p>
<ul>
<li>backup_data (dict): the data to load. use the backup_tiebreak method to obtain this</li>
</ul>
<p><strong>Example</strong></p>
<pre lang="python3"><span class="c1">#backup old data</span>
<span class="n">match</span> <span class="o">=</span> <span class="n">tiebreak</span><span class="p">(</span><span class="s2">"a"</span><span class="p">,</span><span class="s2">"b"</span><span class="p">,{</span><span class="s2">"first_to_num_points"</span><span class="p">:</span><span class="mi">7</span><span class="p">,</span> <span class="s2">"win_by"</span><span class="p">:</span><span class="mi">2</span><span class="p">,</span> <span class="s2">"whos_serve"</span><span class="p">:</span><span class="s2">"a"</span><span class="p">})</span>
<span class="n">backup_data</span> <span class="o">=</span> <span class="n">match</span><span class="o">.</span><span class="n">backup_tiebreak</span><span class="p">()</span>

<span class="c1">#create new tiebreak</span>
<span class="n">new_tiebreak</span> <span class="o">=</span> <span class="n">tiebreak</span><span class="p">(</span><span class="s2">"player1"</span><span class="p">,</span><span class="s2">"player2"</span><span class="p">)</span>

<span class="c1">#load data into new tiebreak</span>
<span class="n">new_tiebreak</span> <span class="o">=</span> <span class="n">new_tiebreak</span><span class="o">.</span><span class="n">load_backup</span><span class="p">(</span><span class="n">backup_data</span><span class="p">)</span>

<span class="c1">#print out stats of old tiebreak</span>
<span class="nb">print</span><span class="p">(</span><span class="n">new_tiebreak</span><span class="o">.</span><span class="n">tiebreak_stats</span><span class="p">(</span><span class="s2">"a"</span><span class="p">))</span>
</pre>
<br>
<hr>
<br>
<h4><a href="https://pypi.org/project/tennis/0.1.2/#win_point" rel="nofollow"><code>win_point</code></a> (self, player:str, how_won=[])</h4>
<p>method that handles a player winning or loosing a point. Do not call this method if it is a double fault. Instead, call the <a href="https://pypi.org/project/tennis/0.1.2/#serve_fault-self-playerstr" rel="nofollow"><code>serve_fault</code> (self, player:str)</a> method
<strong>Parameters</strong></p>
<ul>
<li>player (str): The name of the player who won the point.</li>
<li>how_won (Array): How the point was won (more than 1 in a method call is ok, just append them to the end of the list like ['winner','win_by_volley'])
<ul>
<li><code>Ace</code>: player A wins by by acing player b (Player A's serves the ball in and player B does not even touch the ball)</li>
<li><code>winner</code>: player A wins the point by hitting a winner. (The opponent doesnt touch the ball at all)</li>
<li><code>unforced_error</code>: player A wins the point because player B made an unforced error (An error that was not caused by player A. For example player B got an easy ball and missed it)</li>
<li><code>win_by_volley</code>: player A wins the point on a volley (Hitting the ball when it hasnt bounced right out of the air)</li>
<li><code>win_by_dropshot</code>: player A wins the point with a dropshot (player A lightly hits a short ball close to the net)</li>
<li><code>win_by_overhead</code>: player A wins the point via an overhead (player A "smashes" the ball right out of the air)</li>
</ul>
</li>
</ul>
<p><strong>Example</strong></p>
<pre lang="python3"><span class="k">match</span><span class="o">.</span><span class="n">win_point</span><span class="p">(</span><span class="s2">"a"</span><span class="p">)</span>
<span class="k">match</span><span class="o">.</span><span class="n">win_point</span><span class="p">(</span><span class="s2">"b"</span><span class="p">,</span> <span class="p">[</span><span class="s1">'win_by_volley'</span><span class="p">])</span>
<span class="k">match</span><span class="o">.</span><span class="n">win_point</span><span class="p">(</span><span class="s2">"b"</span><span class="p">,</span> <span class="p">[</span><span class="s1">'win_by_volley'</span><span class="p">,</span><span class="s1">'winner'</span><span class="p">])</span>
</pre>
<br>
<hr>
<br>
<h4><a href="https://pypi.org/project/tennis/0.1.2/#tiebreak_stats" rel="nofollow"><code>tiebreak_stats</code></a> (self, player:str)</h4>
<p>A method that returns a string representation of the statistics of the tiebreak</p>
<p><strong>Parameters</strong></p>
<ul>
<li>player (str): the name of the player whos stats will be displayed on the left side</li>
</ul>
<p><strong>Example</strong></p>
<pre lang="python3"><span class="nb">print</span><span class="p">(</span><span class="n">tb</span><span class="o">.</span><span class="n">tiebreak_stats</span><span class="p">(</span><span class="s2">"a"</span><span class="p">))</span>
</pre>
<br>
<hr>
<br>
<h4><a href="https://pypi.org/project/tennis/0.1.2/#get_scoreboard" rel="nofollow"><code>get_scoreboard</code></a> (self, player:str)</h4>
<p>A method that returns a string representation of the current score</p>
<p><strong>Parameters</strong></p>
<ul>
<li>player (str): the name of the player whos stats will be displayed on the top of the scoreboard</li>
</ul>
<p><strong>Example</strong></p>
<pre lang="python3"><span class="nb">print</span><span class="p">(</span><span class="n">match</span><span class="o">.</span><span class="n">get_scoreboard</span><span class="p">(</span><span class="s2">"a"</span><span class="p">))</span>
</pre>
<p><strong>output:</strong></p>
<pre lang="python3"><span class="err">╔═════════════════════════════════════╗</span>
              <span class="n">Match</span> <span class="n">Score</span>

    <span class="n">M</span>  <span class="n">S</span>  <span class="n">G</span>  <span class="n">T</span>
    <span class="mi">1</span>  <span class="mi">0</span>  <span class="mi">0</span>  <span class="mi">1</span>                  <span class="n">a</span>
    <span class="mi">1</span>  <span class="mi">0</span>  <span class="mi">0</span>  <span class="mi">4</span> <span class="o">*</span>                <span class="n">b</span>

<span class="err">╚═════════════════════════════════════╝</span>
</pre>

          </div>
          
        </div>

        
        <div id="data" data-project-tabs-target="content" class="vertical-tabs__content" role="tabpanel" aria-labelledby="mobile-data-tab" tabindex="-1" style="display: none;">
          <h2 class="page-title">Project details</h2>
          
<div class="sidebar-section">
  <h3 class="sidebar-section__title">Project links</h3>
  <ul class="vertical-tabs__list">
    
    
    <li>
      <a class="vertical-tabs__tab vertical-tabs__tab--with-icon vertical-tabs__tab--condensed" href="https://github.com/bear102/tennis" rel="nofollow">
        


  


<i class="fas fa-home" aria-hidden="true"></i>Homepage
      </a>
    </li>
    
    
  </ul>
</div>


<div class="sidebar-section">
  <h3 class="sidebar-section__title">Statistics</h3>
  
  <div class="hidden github-repo-info" data-controller="github-repo-info">
    GitHub statistics:
    <ul class="vertical-tabs__list">
      <li>
        <a class="vertical-tabs__tab vertical-tabs__tab--with-icon vertical-tabs__tab--condensed" data-github-repo-info-target="stargazersUrl" rel="noopener">
          <i class="fa fa-star" aria-hidden="true"></i>
          <strong>Stars:</strong>
          <span data-github-repo-info-target="stargazersCount"></span>
        </a>
      </li>
      <li>
        <a class="vertical-tabs__tab vertical-tabs__tab--with-icon vertical-tabs__tab--condensed" data-github-repo-info-target="forksUrl" rel="noopener">
          <i class="fa fa-code-branch" aria-hidden="true"></i>
          <strong>Forks:</strong>
          <span data-github-repo-info-target="forksCount"></span>
        </a>
      </li>
      <li>
        <a class="vertical-tabs__tab vertical-tabs__tab--with-icon vertical-tabs__tab--condensed" data-github-repo-info-target="openIssuesUrl" rel="noopener">
          <i class="fa fa-exclamation-circle" aria-hidden="true"></i>
          <strong>Open issues:</strong>
          <span data-github-repo-info-target="openIssuesCount"></span>
        </a>
      </li>
      <li>
        <a class="vertical-tabs__tab vertical-tabs__tab--with-icon vertical-tabs__tab--condensed" data-github-repo-info-target="openPRsUrl" rel="noopener">
          <i class="fa fa-code-pull-request" aria-hidden="true"></i>
          <strong>Open PRs:</strong>
          <span data-github-repo-info-target="openPRsCount"></span>
        </a>
      </li>
    </ul>
  </div>
  
  <p>
    View statistics for this project via <a href="https://libraries.io/pypi/tennis" title="External link" target="_blank" rel="noopener">Libraries.io</a>, or by using <a href="https://packaging.python.org/guides/analyzing-pypi-package-downloads/" target="_blank" rel="noopener">our public dataset on Google BigQuery</a>
  </p>
</div>


<div class="sidebar-section">
  <h3 class="sidebar-section__title">Meta</h3>
  
  <p><strong>License:</strong> MIT License (MIT)</p>
  
  
    <p><strong>Author:</strong> bear102</p>
  
  
  
  
  <p>
    <strong>Requires:</strong> Python &gt;=3.7
  </p>
  
</div>


<div class="sidebar-section">
  
  
    <h3 class="sidebar-section__title">Maintainers</h3>
    
      
      <span class="sidebar-section__maintainer">
        <a href="https://pypi.org/user/bear102/" aria-label="bear102">
          <span class="sidebar-section__user-gravatar">
            <img src="./rm_files/68747470733a2f2f7365637572652e67726176617461722e636f6d2f6176617461722f34343565303366666433613432366538636662393566343136386266393034393f73697a653d3530" height="50" width="50" alt="Avatar for bear102 from gravatar.com" title="Avatar for bear102 from gravatar.com">
          </span>
          <span class="sidebar-section__user-gravatar-text">
            bear102
          </span>
        </a>
      </span>
    
  
</div>


<div class="sidebar-section">
  <h3 class="sidebar-section__title">Classifiers</h3>
  <ul class="sidebar-section__classifiers">
    
    <li>
      <strong>License</strong>
      <ul>
        
        <li>
          <a href="https://pypi.org/search/?c=License+%3A%3A+OSI+Approved+%3A%3A+MIT+License">
            OSI Approved :: MIT License
          </a>
        </li>
        
      </ul>
    </li>
    
    <li>
      <strong>Operating System</strong>
      <ul>
        
        <li>
          <a href="https://pypi.org/search/?c=Operating+System+%3A%3A+OS+Independent">
            OS Independent
          </a>
        </li>
        
      </ul>
    </li>
    
    <li>
      <strong>Programming Language</strong>
      <ul>
        
        <li>
          <a href="https://pypi.org/search/?c=Programming+Language+%3A%3A+Python+%3A%3A+3">
            Python :: 3
          </a>
        </li>
        
      </ul>
    </li>
    
  </ul>
</div>

          <br>
        </div>

        
        <div id="history" data-project-tabs-target="content" class="vertical-tabs__content" role="tabpanel" aria-labelledby="history-tab mobile-history-tab" tabindex="-1" style="display: none;">
          <h2 class="page-title split-layout">
            <span>Release history</span>
            <span class="reset-text margin-top">
              <a href="https://pypi.org/help/#project-release-notifications">Release notifications</a> |
              <a href="https://pypi.org/rss/project/tennis/releases.xml">RSS feed <i class="fa fa-rss" aria-hidden="true"></i></a>
            </span>
          </h2>

          <div class="release-timeline">
            
            
            
            
            <div class="release release--latest release--current">
              <div class="release__meta">
                
                <span class="badge">This version</span>
                
              </div>

              <div class="release__graphic">
                
                <div class="release__line"></div>
                
                
                <img class="release__node" alt="" src="./rm_files/blue-cube.572a5bfb.svg">
                
              </div>

              <a class="card release__card" href="https://pypi.org/project/tennis/0.1.2/">
                <p class="release__version">
                  0.1.2
                  
                  
                </p>
                <p class="release__version-date">
                  <time datetime="2023-05-11T02:26:45+0000" data-controller="localized-time" data-localized-time-relative="true" data-localized-time-show-time="false" title="2023-05-10 21:26:45 (-05:00)" aria-label="2023-05-10 21:26:45 (-05:00)">3 minutes ago</time>
                </p>
              </a>
            </div>
            
            
            <div class="release">
              <div class="release__meta">
                
              </div>

              <div class="release__graphic">
                
                <div class="release__line"></div>
                
                
                <img class="release__node" alt="" src="./rm_files/white-cube.2351a86c.svg">
                
              </div>

              <a class="card release__card" href="https://pypi.org/project/tennis/0.1.1/">
                <p class="release__version">
                  0.1.1
                  
                  
                </p>
                <p class="release__version-date">
                  <time datetime="2023-05-10T21:44:02+0000" data-controller="localized-time" data-localized-time-relative="true" data-localized-time-show-time="false" title="2023-05-10 16:44:02 (-05:00)" aria-label="2023-05-10 16:44:02 (-05:00)">May 10, 2023</time>
                </p>
              </a>
            </div>
            
            
            <div class="release release--oldest">
              <div class="release__meta">
                
              </div>

              <div class="release__graphic">
                
                <div class="release__line"></div>
                
                
                <img class="release__node" alt="" src="./rm_files/white-cube.2351a86c.svg">
                
              </div>

              <a class="card release__card" href="https://pypi.org/project/tennis/0.1.0/">
                <p class="release__version">
                  0.1.0
                  
                  
                </p>
                <p class="release__version-date">
                  <time datetime="2023-05-09T03:52:26+0000" data-controller="localized-time" data-localized-time-relative="true" data-localized-time-show-time="false" title="2023-05-08 22:52:26 (-05:00)" aria-label="2023-05-08 22:52:26 (-05:00)">May 8, 2023</time>
                </p>
              </a>
            </div>
            
          </div>
        </div>

        
          
          <div id="files" data-project-tabs-target="content" class="vertical-tabs__content" role="tabpanel" aria-labelledby="files-tab mobile-files-tab" tabindex="-1" style="display: none;">
            <h2 class="page-title">Download files</h2>
            <p>Download the file for your platform. If you're not sure which to choose, learn more about <a href="https://packaging.python.org/installing/" title="External link" target="_blank" rel="noopener">installing packages</a>.</p>
            <h3>
              Source Distribution
            </h3>

            
              
    <div class="file">
      <div class="file__graphic">
        <i class="far fa-file" aria-hidden="true"></i>
      </div>

      <div class="card file__card">
        <a href="https://files.pythonhosted.org/packages/0b/8d/4be915c92a3180a461b3d8ecb78839a5a91fd1f5f769fac6d737590696bb/tennis-0.1.2.tar.gz">
          tennis-0.1.2.tar.gz
        </a>
        (15.0 kB
        <a href="https://pypi.org/project/tennis/0.1.2/#copy-hash-modal-4621beb3-3725-42c6-bf76-90eabfe8488d">view hashes</a>)
        <p class="file__meta">
          Uploaded <time datetime="2023-05-11T02:26:48+0000" data-controller="localized-time" data-localized-time-relative="true" data-localized-time-show-time="false" title="2023-05-10 21:26:48 (-05:00)" aria-label="2023-05-10 21:26:48 (-05:00)">3 minutes ago</time>
          
          
          <code>source</code>
          
          
        </p>
      </div>
    </div>
  
            

            
            <h3>
              Built Distribution
            </h3>

            
    <div class="file">
      <div class="file__graphic">
        <i class="far fa-file" aria-hidden="true"></i>
      </div>

      <div class="card file__card">
        <a href="https://files.pythonhosted.org/packages/a0/0f/4e0a055cc8d2971d19653bb33fa099eef4aedd2c7e32715de82984e93a19/tennis-0.1.2-py3-none-any.whl">
          tennis-0.1.2-py3-none-any.whl
        </a>
        (13.6 kB
        <a href="https://pypi.org/project/tennis/0.1.2/#copy-hash-modal-cc8b06b8-29b1-4ca1-a6dc-f6b48de1ac9d">view hashes</a>)
        <p class="file__meta">
          Uploaded <time datetime="2023-05-11T02:26:45+0000" data-controller="localized-time" data-localized-time-relative="true" data-localized-time-show-time="false" title="2023-05-10 21:26:45 (-05:00)" aria-label="2023-05-10 21:26:45 (-05:00)">3 minutes ago</time>
          
          
          <code>py3</code>
          
          
        </p>
      </div>
    </div>
  
            
          </div>

          
          <div id="copy-hash-modal-4621beb3-3725-42c6-bf76-90eabfe8488d" class="modal modal--wide">
  <div class="modal__content" role="dialog">
    <a href="https://pypi.org/project/tennis/0.1.2/#modal-close" title="Close" class="modal__close">
      <i class="fa fa-times" aria-hidden="true"></i>
      <span class="sr-only">Close</span>
    </a>
    <div class="modal__body">
      <h3 class="modal__title">
        <a href="https://pip.pypa.io/en/stable/cli/pip_install/#hash-checking-mode" title="External link" target="_blank" rel="noopener">Hashes</a> for tennis-0.1.2.tar.gz
      </h3>
      <table class="table table--hashes">
        <caption class="sr-only">Hashes for tennis-0.1.2.tar.gz</caption>
        <thead>
          <tr>
            <th scope="col">Algorithm</th>
            <th scope="col">Hash digest</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          <tr data-controller="clipboard">
            <th scope="row">SHA256</th>
            <td><code data-clipboard-target="source">2b402105ddfac9c7dbcaa7bf76748cd1ae8f58ede70f5914f8f3c3485392c5e7</code></td>
            <td class="table__align-right">
              <button type="button" class="button button--small copy-tooltip copy-tooltip-w" data-action="clipboard#copy" data-clipboard-target="tooltip" data-clipboard-tooltip-value="Copy to clipboard">
                Copy
              </button>
            </td>
          </tr>
          <tr data-controller="clipboard">
            <th scope="row">MD5</th>
            <td><code data-clipboard-target="source">3c99559dbd4a08ce070f1451aeb8d8df</code></td>
            <td class="table__align-right">
              <button type="button" class="button button--small copy-tooltip copy-tooltip-w" data-action="clipboard#copy" data-clipboard-target="tooltip" data-clipboard-tooltip-value="Copy to clipboard">
                Copy
              </button>
            </td>
          </tr>
          <tr data-controller="clipboard">
            <th scope="row">BLAKE2b-256</th>
            <td><code data-clipboard-target="source">0b8d4be915c92a3180a461b3d8ecb78839a5a91fd1f5f769fac6d737590696bb</code></td>
            <td class="table__align-right">
              <button type="button" class="button button--small copy-tooltip copy-tooltip-w" data-action="clipboard#copy" data-clipboard-target="tooltip" data-clipboard-tooltip-value="Copy to clipboard">
                Copy
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="modal__footer">
      <a href="https://pypi.org/project/tennis/0.1.2/#modal-close" class="button button--primary modal__action">Close</a>
    </div>
  </div>
</div>
          
          <div id="copy-hash-modal-cc8b06b8-29b1-4ca1-a6dc-f6b48de1ac9d" class="modal modal--wide">
  <div class="modal__content" role="dialog">
    <a href="https://pypi.org/project/tennis/0.1.2/#modal-close" title="Close" class="modal__close">
      <i class="fa fa-times" aria-hidden="true"></i>
      <span class="sr-only">Close</span>
    </a>
    <div class="modal__body">
      <h3 class="modal__title">
        <a href="https://pip.pypa.io/en/stable/cli/pip_install/#hash-checking-mode" title="External link" target="_blank" rel="noopener">Hashes</a> for tennis-0.1.2-py3-none-any.whl
      </h3>
      <table class="table table--hashes">
        <caption class="sr-only">Hashes for tennis-0.1.2-py3-none-any.whl</caption>
        <thead>
          <tr>
            <th scope="col">Algorithm</th>
            <th scope="col">Hash digest</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          <tr data-controller="clipboard">
            <th scope="row">SHA256</th>
            <td><code data-clipboard-target="source">243e10a24eab039db0cea635650f7736b107124557752b14d8ae786a8e90fc9c</code></td>
            <td class="table__align-right">
              <button type="button" class="button button--small copy-tooltip copy-tooltip-w" data-action="clipboard#copy" data-clipboard-target="tooltip" data-clipboard-tooltip-value="Copy to clipboard">
                Copy
              </button>
            </td>
          </tr>
          <tr data-controller="clipboard">
            <th scope="row">MD5</th>
            <td><code data-clipboard-target="source">383f2fa90dc3c2fa80c04a8727c08573</code></td>
            <td class="table__align-right">
              <button type="button" class="button button--small copy-tooltip copy-tooltip-w" data-action="clipboard#copy" data-clipboard-target="tooltip" data-clipboard-tooltip-value="Copy to clipboard">
                Copy
              </button>
            </td>
          </tr>
          <tr data-controller="clipboard">
            <th scope="row">BLAKE2b-256</th>
            <td><code data-clipboard-target="source">a00f4e0a055cc8d2971d19653bb33fa099eef4aedd2c7e32715de82984e93a19</code></td>
            <td class="table__align-right">
              <button type="button" class="button button--small copy-tooltip copy-tooltip-w" data-action="clipboard#copy" data-clipboard-target="tooltip" data-clipboard-tooltip-value="Copy to clipboard">
                Copy
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="modal__footer">
      <a href="https://pypi.org/project/tennis/0.1.2/#modal-close" class="button button--primary modal__action">Close</a>
    </div>
  </div>
</div>
          

        
      </div>
    </div>
  </div>
</div>

    </main>

    <footer class="footer">
      <div class="footer__logo">
        <img src="./rm_files/white-cube.2351a86c.svg" alt="" class="-js-white-cube">
      </div>

      <div class="footer__menus">
        <div class="footer__menu">
          <h2>Help</h2>
          <nav aria-label="Help navigation">
            <ul>
              <li><a href="https://packaging.python.org/installing/" title="External link" target="_blank" rel="noopener">Installing packages</a></li>
              <li><a href="https://packaging.python.org/tutorials/packaging-projects/" title="External link" target="_blank" rel="noopener">Uploading packages</a></li>
              <li><a href="https://packaging.python.org/" title="External link" target="_blank" rel="noopener">User guide</a></li>
              <li><a href="https://www.python.org/dev/peps/pep-0541/" title="External link" target="_blank" rel="noopener">Project name retention</a></li>
              <li><a href="https://pypi.org/help/">FAQs</a></li>
            </ul>
          </nav>
        </div>

        <div class="footer__menu">
          <h2>About PyPI</h2>
          <nav aria-label="About PyPI navigation">
            <ul>
              <li><a href="https://twitter.com/PyPI" title="External link" target="_blank" rel="noopener">PyPI on Twitter</a></li>
              <li><a href="https://dtdg.co/pypi" title="External link" target="_blank" rel="noopener">Infrastructure dashboard</a></li>
              <li><a href="https://pypi.org/stats/">Statistics</a></li>
              <li><a href="https://pypi.org/trademarks/">Logos &amp; trademarks</a></li>
              <li><a href="https://pypi.org/sponsors/">Our sponsors</a></li>
            </ul>
          </nav>
        </div>

        <div class="footer__menu">
          <h2>Contributing to PyPI</h2>
          <nav aria-label="How to contribute navigation">
            <ul>
              <li><a href="https://pypi.org/help/#feedback">Bugs and feedback</a></li>
              <li><a href="https://github.com/pypi/warehouse" title="External link" target="_blank" rel="noopener">Contribute on GitHub</a></li>
              <li><a href="https://hosted.weblate.org/projects/pypa/warehouse/" title="External link" target="_blank" rel="noopener">Translate PyPI</a></li>
              <li><a href="https://pypi.org/sponsors/">Sponsor PyPI</a></li>
              <li><a href="https://github.com/pypi/warehouse/graphs/contributors" title="External link" target="_blank" rel="noopener">Development credits</a></li>
            </ul>
          </nav>
        </div>

        <div class="footer__menu">
          <h2>Using PyPI</h2>
          <nav aria-label="Using PyPI navigation">
            <ul>
              <li><a href="https://github.com/pypa/.github/blob/main/CODE_OF_CONDUCT.md" title="External link" target="_blank" rel="noopener">Code of conduct</a></li>
              <li><a href="https://pypi.org/security/">Report security issue</a></li>
              <li><a href="https://www.python.org/privacy/" title="External link" target="_blank" rel="noopener">Privacy policy</a></li>
              <li><a href="https://pypi.org/policy/terms-of-use/">Terms of use</a></li>
              <li><a href="https://pypi.org/policy/acceptable-use-policy/">Acceptable Use Policy</a></li>
            </ul>
          </nav>
        </div>
      </div>

      <hr class="footer__divider">

      <div class="footer__text">
        
        <p>Status:<a href="https://status.python.org/" title="External link" target="_blank" rel="noopener">
          <span data-statuspage-domain="https://2p66nmmycsj3.statuspage.io">Service Under Maintenance</span></a>
        </p>
        
        <p>
          Developed and maintained by the Python community, for the Python community.
          <br>
          <a href="https://donate.pypi.org/">Donate today!</a>
        </p>
        <p>
          
"PyPI", "Python Package Index", and the blocks logos are registered <a href="https://pypi.org/trademarks/">trademarks</a> of the <a href="https://python.org/psf-landing" target="_blank" rel="noopener">Python Software Foundation</a>.
<br>
        </p>
        <p>
          © 2023 <a href="https://www.python.org/psf-landing/" title="External link" target="_blank" rel="noopener">Python Software Foundation</a><br>
          <a href="https://pypi.org/sitemap/">Site map</a>
        </p>
      </div>

      <div class="centered hide-on-desktop">
        <button type="button" class="button button--switch-to-desktop" data-viewport-toggle-target="switchToDesktop" data-action="viewport-toggle#switchToDesktop">
          Switch to desktop version
        </button>
      </div>
    </footer>


    <div class="language-switcher">
      <form action="https://pypi.org/locale/">
        <ul>
          
          <li>
            <button class="language-switcher__selected" name="locale_id" value="en" type="submit">
              English
            </button>
          </li>
          
          <li>
            <button name="locale_id" value="es" type="submit">
              español
            </button>
          </li>
          
          <li>
            <button name="locale_id" value="fr" type="submit">
              français
            </button>
          </li>
          
          <li>
            <button name="locale_id" value="ja" type="submit">
              日本語
            </button>
          </li>
          
          <li>
            <button name="locale_id" value="pt_BR" type="submit">
              português (Brasil)
            </button>
          </li>
          
          <li>
            <button name="locale_id" value="uk" type="submit">
              українська
            </button>
          </li>
          
          <li>
            <button name="locale_id" value="el" type="submit">
              Ελληνικά
            </button>
          </li>
          
          <li>
            <button name="locale_id" value="de" type="submit">
              Deutsch
            </button>
          </li>
          
          <li>
            <button name="locale_id" value="zh_Hans" type="submit">
              中文 (简体)
            </button>
          </li>
          
          <li>
            <button name="locale_id" value="zh_Hant" type="submit">
              中文 (繁體)
            </button>
          </li>
          
          <li>
            <button name="locale_id" value="ru" type="submit">
              русский
            </button>
          </li>
          
          <li>
            <button name="locale_id" value="he" type="submit">
              עברית
            </button>
          </li>
          
          <li>
            <button name="locale_id" value="eo" type="submit">
              esperanto
            </button>
          </li>
          
        </ul>
      </form>
    </div>


    <div class="sponsors">
  <p class="sponsors__title">Supported by</p>
  
    
    
  
    
    
  
    
    
  
    
    
  
    
    
  
    
    
  
    
    
  
    
    
  
    
    
  
    
    
      
      
        <a class="sponsors__sponsor" target="_blank" rel="noopener" href="https://aws.amazon.com/">
          <img class="sponsors__image" src="./rm_files/68747470733a2f2f73746f726167652e676f6f676c65617069732e636f6d2f707970692d6173736574732f73706f6e736f726c6f676f732f6177732d77686974652d6c6f676f2d7443615473387a432e706e67" alt="AWS" loading="lazy">
          <span class="sponsors__name">AWS</span>
          <span class="sponsors__service">
          
          
            Cloud computing and Security Sponsor
          
          </span>
        </a>
      
    
  
    
    
  
    
    
      
      
    
  
    
    
  
    
    
  
    
    
  
    
    
  
    
    
  
    
    
  
    
    
      
      
    
  
    
    
  
    
    
  
    
    
  
    
    
      
      
    
  
    
    
  
    
    
  
    
    
  
    
    
  
    
    
      
      
        <a class="sponsors__sponsor" target="_blank" rel="noopener" href="https://www.datadoghq.com/">
          <img class="sponsors__image" src="./rm_files/68747470733a2f2f73746f726167652e676f6f676c65617069732e636f6d2f707970692d6173736574732f73706f6e736f726c6f676f732f64617461646f672d77686974652d6c6f676f2d6668644c4e666c6f2e706e67" alt="Datadog" loading="lazy">
          <span class="sponsors__name">Datadog</span>
          <span class="sponsors__service">
          
          
            Monitoring
          
          </span>
        </a>
      
    
  
    
    
  
    
    
  
    
    
  
    
    
  
    
    
      
      
    
  
    
    
      
      
    
  
    
    
  
    
    
      
      
        <a class="sponsors__sponsor" target="_blank" rel="noopener" href="https://www.fastly.com/">
          <img class="sponsors__image" src="./rm_files/68747470733a2f2f73746f726167652e676f6f676c65617069732e636f6d2f707970692d6173736574732f73706f6e736f726c6f676f732f666173746c792d77686974652d6c6f676f2d65684d3077735f6f2e706e67" alt="Fastly" loading="lazy">
          <span class="sponsors__name">Fastly</span>
          <span class="sponsors__service">
          
          
            CDN
          
          </span>
        </a>
      
    
  
    
    
  
    
    
      
      
        <a class="sponsors__sponsor" target="_blank" rel="noopener" href="https://careers.google.com/">
          <img class="sponsors__image" src="./rm_files/68747470733a2f2f73746f726167652e676f6f676c65617069732e636f6d2f707970692d6173736574732f73706f6e736f726c6f676f732f676f6f676c652d77686974652d6c6f676f2d616734424e3774332e706e67" alt="Google" loading="lazy">
          <span class="sponsors__name">Google</span>
          <span class="sponsors__service">
          
          
            Download Analytics
          
          </span>
        </a>
      
    
  
    
    
  
    
    
  
    
    
  
    
    
  
    
    
  
    
    
  
    
    
      
      
    
  
    
    
  
    
    
  
    
    
  
    
    
  
    
    
      
      
        <a class="sponsors__sponsor" target="_blank" rel="noopener" href="https://www.python.org/psf/sponsors/#microsoft">
          <img class="sponsors__image" src="./rm_files/68747470733a2f2f73746f726167652e676f6f676c65617069732e636f6d2f707970692d6173736574732f73706f6e736f726c6f676f732f6d6963726f736f66742d77686974652d6c6f676f2d5a443172685444462e706e67" alt="Microsoft" loading="lazy">
          <span class="sponsors__name">Microsoft</span>
          <span class="sponsors__service">
          
          
            PSF Sponsor
          
          </span>
        </a>
      
    
  
    
    
  
    
    
  
    
    
  
    
    
  
    
    
      
      
    
  
    
    
  
    
    
  
    
    
  
    
    
  
    
    
  
    
    
  
    
    
      
      
        <a class="sponsors__sponsor" target="_blank" rel="noopener" href="https://www.pingdom.com/">
          <img class="sponsors__image" src="./rm_files/68747470733a2f2f73746f726167652e676f6f676c65617069732e636f6d2f707970692d6173736574732f73706f6e736f726c6f676f732f70696e67646f6d2d77686974652d6c6f676f2d67355831547546362e706e67" alt="Pingdom" loading="lazy">
          <span class="sponsors__name">Pingdom</span>
          <span class="sponsors__service">
          
          
            Monitoring
          
          </span>
        </a>
      
    
  
    
    
  
    
    
  
    
    
  
    
    
  
    
    
  
    
    
  
    
    
  
    
    
  
    
    
  
    
    
  
    
    
  
    
    
  
    
    
  
    
    
      
      
    
  
    
    
  
    
    
  
    
    
      
      
        <a class="sponsors__sponsor" target="_blank" rel="noopener" href="https://getsentry.com/for/python">
          <img class="sponsors__image" src="./rm_files/68747470733a2f2f73746f726167652e676f6f676c65617069732e636f6d2f707970692d6173736574732f73706f6e736f726c6f676f732f73656e7472792d77686974652d6c6f676f2d31556836754c32452e706e67" alt="Sentry" loading="lazy">
          <span class="sponsors__name">Sentry</span>
          <span class="sponsors__service">
          
          
            Error logging
          
          </span>
        </a>
      
    
  
    
    
  
    
    
  
    
    
  
    
    
  
    
    
  
    
    
  
    
    
  
    
    
  
    
    
      
      
        <a class="sponsors__sponsor" target="_blank" rel="noopener" href="https://statuspage.io/">
          <img class="sponsors__image" src="./rm_files/68747470733a2f2f73746f726167652e676f6f676c65617069732e636f6d2f707970692d6173736574732f73706f6e736f726c6f676f732f737461747573706167652d77686974652d6c6f676f2d5467476c6a4a2d502e706e67" alt="StatusPage" loading="lazy">
          <span class="sponsors__name">StatusPage</span>
          <span class="sponsors__service">
          
          
            Status page
          
          </span>
        </a>
      
    
  
    
    
  
    
    
  
    
    
  
    
    
  
    
    
  
    
    
  
    
    
  
    
    
  
</div>

    
  

</body></html>
