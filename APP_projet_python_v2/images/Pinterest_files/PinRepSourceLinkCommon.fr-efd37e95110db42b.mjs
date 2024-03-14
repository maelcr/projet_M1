"use strict";(self.__LOADABLE_LOADED_CHUNKS__=self.__LOADABLE_LOADED_CHUNKS__||[]).push([[99429],{309378:e=>{var l,a={argumentDefinitions:[],kind:"Fragment",metadata:null,name:"SourceLink_pin",selections:[{alias:null,args:null,kind:"ScalarField",name:"adDestinationUrl",storageKey:null},{alias:null,args:null,kind:"ScalarField",name:"advertiserId",storageKey:null},{alias:null,args:null,kind:"ScalarField",name:"attributionSourceId",storageKey:null},{alias:null,args:null,concreteType:"Board",kind:"LinkedField",name:"board",plural:!1,selections:[{alias:null,args:null,kind:"ScalarField",name:"url",storageKey:null}],storageKey:null},{alias:null,args:null,kind:"ScalarField",name:"campaignId",storageKey:null},{alias:null,args:null,concreteType:"PinCarouselData",kind:"LinkedField",name:"carouselData",plural:!1,selections:[{alias:null,args:null,concreteType:"PinCarouselSlot",kind:"LinkedField",name:"carouselSlots",plural:!0,selections:[{alias:null,args:null,kind:"ScalarField",name:"link",storageKey:null}],storageKey:null},l={alias:null,args:null,kind:"ScalarField",name:"entityId",storageKey:null},{alias:null,args:null,kind:"ScalarField",name:"index",storageKey:null}],storageKey:null},{alias:null,args:null,kind:"ScalarField",name:"domain",storageKey:null},l,{alias:null,args:null,kind:"ScalarField",name:"isDownstreamPromotion",storageKey:null},{alias:null,args:null,kind:"ScalarField",name:"isPromoted",storageKey:null},{alias:null,args:null,concreteType:"User",kind:"LinkedField",name:"pinner",plural:!1,selections:[{alias:null,args:null,kind:"ScalarField",name:"username",storageKey:null}],storageKey:null},{alias:null,args:null,kind:"ScalarField",name:"pinPromotionId",storageKey:null},{alias:null,args:null,concreteType:"User",kind:"LinkedField",name:"promoter",plural:!1,selections:[l],storageKey:null},{alias:null,args:null,kind:"ScalarField",name:"storyPinDataId",storageKey:null},{alias:null,args:null,kind:"ScalarField",name:"trackingParams",storageKey:null},{args:null,kind:"FragmentSpread",name:"ContextMenuClickthroughLogging_pin"},{args:null,kind:"FragmentSpread",name:"useGetStringifiedCommerceAuxData_pin"}],type:"Pin",abstractKey:null};a.hash="b73ff04162d730bc3f23d71ed736b3f9",e.exports=a},787051:(e,l,a)=>{a.r(l),a.d(l,{default:()=>I,styles:()=>h});var n,i=a(667294);a(167912);var r=a(616550),t=a(883119),o=a(41282),s=a(768559),d=a(413614),u=a(916117),c=a(898781),g=a(287072),m=a(773285),y=a(780280),p=a(999018),_=a(199387),k=a(576440),b=a(89254),x=a(785893);let h={container:{backgroundColor:"rgba(255, 255, 255, 0.9)",borderRadius:18,height:"32px",maxWidth:"132px"},containerHovered:{backgroundColor:"rgba(255, 255, 255, 1.0)"},containerTruncated:{maxWidth:"87px"},text:{color:"#333333"}},S=void 0!==n?n:n=a(309378);function I({pinKey:e,sourceLinkStyle:l,surface:a,trackingParamsMap:n,url:I}){var f,v,P,D,F,K;let L=(0,c.ZP)(),[w,j]=(0,i.useState)(!1),C=(0,u.Z)(S,e),T=(null===(f=C.carouselData)||void 0===f?void 0:f.index)||0,{isAuthenticated:Z}=(0,y.B)(),{checkExperiment:A}=(0,m.F)(),z=Z&&A("web_obfuscate_offsite_url_in_href").anyEnabled,{entityId:U}=C,E=function({adDestinationUrl:e,domain:l,carouselDataId:a,carouselSlotLink:n}){let i=l||"";return e&&(i=(0,b.Z)(e).hostname||""),a&&(i=n&&(0,b.Z)(n).hostname||""),i.replace("www.","")}({adDestinationUrl:C.adDestinationUrl,domain:C.domain,carouselDataId:null===(v=C.carouselData)||void 0===v?void 0:v.entityId,carouselSlotLink:null===(P=C.carouselData)||void 0===P?void 0:null===(D=P.carouselSlots)||void 0===D?void 0:D[T].link}),O=(0,r.TH)(),W=(0,p.Z)(C),B=W(),{slotIndex:H}=(0,k.E)(),M=(0,s.Z)({boardUrl:null===(F=C.board)||void 0===F?void 0:F.url,location:O,pinId:C.entityId,pinnerUserName:null===(K=C.pinner)||void 0===K?void 0:K.username,storyPinDataId:C.storyPinDataId,trackingParams:C.trackingParams,trackingParamsMap:n}),N=(0,_.Z)(12,{object_id_str:U,clientTrackingParams:M,aux_data:{grid_index:H,...B}}),G=(0,_.Z)(101,{element:162,object_id_str:U,clientTrackingParams:M,aux_data:{...B}}),J=(0,_.Z)(8948,{object_id_str:U,clientTrackingParams:M,aux_data:{click_type:"clickthrough",closeup_navigation_type:"click",grid_index:H,...B}}),R=()=>{N(),G(),J()},q=(0,g.Z)({href:I,target:"blank",externalData:{auxData:B,pin:C&&{advertiserId:C.advertiserId,attributionSourceId:C.attributionSourceId,board:C.board&&{url:C.board.url},campaignId:C.campaignId,entityId:C.entityId,isDownstreamPromotion:C.isDownstreamPromotion,isPromoted:C.isPromoted,pinner:C.pinner&&{username:C.pinner.username},pinPromotionId:C.pinPromotionId,promoter:C.promoter&&{entityId:C.promoter.entityId},storyPinDataId:C.storyPinDataId,trackingParams:C.trackingParams,trackingParamsMap:n},surface:a}});return"icon-only"===l?(0,x.jsx)(t.I_,{accessibilityLabel:L.bt("lien", "link", "Website url link", undefined, true),bgColor:"white",href:I,icon:"arrow-up-right",iconColor:"darkGray",onClick:({event:e,dangerouslyDisableOnNavigation:l})=>{l(),R(),q({event:e})},rel:"nofollow",size:"sm"}):(0,x.jsx)(t.xu,{dangerouslySetInlineStyle:{__style:{...h.container,...w?h.containerHovered:Object.freeze({}),..."truncated-text"===l?h.containerTruncated:Object.freeze({})}},"data-test-id":"pinrep-source-link",onMouseEnter:()=>j(!0),onMouseLeave:()=>j(!1),position:"relative",children:(0,x.jsx)(d.Z,{hovered:w,pinKey:C,slotIndex:H,trackingParamsMap:n,viewType:1,children:(0,x.jsx)(t.Tg,{fullWidth:!1,href:z?(0,o.Z)(I):I,onTap:({event:e,dangerouslyDisableOnNavigation:l})=>{l(),R(),q({event:e})},rel:"nofollow",rounding:4,children:(0,x.jsxs)(t.xu,{alignItems:"baseline",dangerouslySetInlineStyle:{__style:h.text},display:"flex",justifyContent:"between",children:[(0,x.jsx)(t.xu,{display:"flex",flex:"none",marginBottom:3,marginStart:3,marginTop:3,children:(0,x.jsx)(t.JO,{accessibilityLabel:L.bt("lien", "link", "Website url link", undefined, true),color:"default",icon:"arrow-up-right",size:9})}),(0,x.jsx)(t.xu,{alignItems:"center",display:"flex",height:18,marginEnd:3,marginStart:2,overflow:"hidden",children:(0,x.jsx)(t.xv,{color:"default",lineClamp:1,size:"200",weight:"bold",children:E})})]})})})})}}}]);
//# sourceMappingURL=https://sm.pinimg.com/webapp/PinRepSourceLinkCommon.fr-efd37e95110db42b.mjs.map