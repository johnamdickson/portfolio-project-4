/**
 * @jest-environment jsdom
 */

(g=>{var h,a,k,p="The Google Maps JavaScript API",c="google",l="importLibrary",q="__ib__",m=document,b=window;b=b[c]||(b[c]={});var d=b.maps||(b.maps={}),r=new Set,e=new URLSearchParams,u=()=>h||(h=new Promise(async(f,n)=>{await (a=m.createElement("script"));e.set("libraries",[...r]+"");for(k in g)e.set(k.replace(/[A-Z]/g,t=>"_"+t[0].toLowerCase()),g[k]);e.set("callback",c+".maps."+q);a.src=`https://maps.${c}apis.com/maps/api/js?`+e;d[q]=f;a.onerror=()=>h=n(Error(p+" could not load."));a.nonce=m.querySelector("script[nonce]")?.nonce||"";m.head.append(a)}));d[l]?console.warn(p+" only loads once. Ignoring:",g):d[l]=(f,...n)=>r.add(f)&&u().then(()=>d[l](f,...n))})
    ({key: "AIzaSyDFRRlo1ePBYrJnuCMcVFvqRJa_9UQMa4I", v: "weekly"});

const errorCountdown = require("../script");

beforeAll(() => {
    let fs = require("fs");
    let fileContents = fs.readFileSync("templates/403.html", "utf-8");
    document.write(fileContents);
    document.close();
});


describe("DOM tests", () => {
    test("Expects timer to be set at 10 seconds", () => {
        errorCountdown();
        expect(document.getElementById("error-timer")
            .innerHTML).toEqual("10");
    });
    test("h2 should exist", () => {
        expect(document.getElementsByTagName("h2").length).toBe(1);
    });
    test("h2 should be 403 error", () => {
        let h2 = document.getElementsByTagName('h2');
        let h2Text = h2[0].innerHTML
        expect(h2Text).toBe("403 Error")
    });
});