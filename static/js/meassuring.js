
    var n = ["image/jpeg", "image/pjpeg", "image/png"];

    function f(e) {
        for (var t = 0; t < n.length; t++)
            if (e.type === n[t]) return !0;
        return !1
    }
/*
    function e(e) {
        return e < 1024 ? e + "bytes" : 1024 <= e && e < 1048576 ? (e / 1024).toFixed(1) + "KB" : 1048576 <= e ? (e / 1048576).toFixed(1) + "MB" : void 0
    }

    function b(e) {
        return /^(?:\w+:)?\/\/([^\s\.]+\.\S{2}|localhost[\:?\d]*)\S*$/.test(e)
    }
*/
    function t(e, l) {
        var t = new FileReader;
        console.log('T ',t);
        t.onload = function(e) {
            var t = new DataView(e.target.result);

            if (65496 != t.getUint16(0, !1)) return l(-2);
            for (var n = t.byteLength, a = 2; a < n;) {
                if (t.getUint16(a + 2, !1) <= 8) return l(-1);
                var r = t.getUint16(a, !1);
                if (a += 2, 65505 == r) {
                    if (1165519206 != t.getUint32(a += 2, !1)) return l(-1);
                    var o = 18761 == t.getUint16(a += 6, !1);
                    a += t.getUint32(a + 4, o);
                    var i = t.getUint16(a, o);
                    a += 2;
                    for (var d = 0; d < i; d++)
                        if (274 == t.getUint16(a + 12 * d, o)) return l(t.getUint16(a + 12 * d + 8, o))
                } else {
                    if (65280 != (65280 & r)) break;
                    a += t.getUint16(a, !1)
                }
            }
            return l(-1)
        }, t.readAsArrayBuffer(e)
    }

    document.addEventListener("DOMContentLoaded", function(e) {
        var o, m = document.getElementById("output"),
            a = document.getElementById("info"),
            t = document.getElementById("ref"),
            r = document.getElementById("save"),
            i = (document.getElementById("overlay"), document.getElementById("canvas"));
            console.log('i', i);
        i.width = parseInt(window.getComputedStyle(i.parentNode, null).getPropertyValue("width"));
        var v = i.getContext("2d"),
            y = [],
            d = !1,
            l = 0,
            s = 0,
            c = new Image;
//            c.src = document.{{plant.scan.url}};
            c.src = document.getElementById('loadbutton').src;



            console.log('c 58 new Image', c);
            console.log('c src', c.src);
        c.crossOrigin = "anonymous", c.referrerPolicy = "no-referrer", c.style.display = "none", c.onload = function() {
            c.width, c.height, i.style.borderRadius = "0", c.width <= i.parentNode.offsetWidth ? i.width = c.width : i.width = parseInt(window.getComputedStyle(i.parentNode, null).getPropertyValue("width")), i.height = i.width * c.height / c.width, v.drawImage(c, 0, 0, c.width, c.height, 0, 0, i.width, i.height), v.lineWidth = 3, y = [], x(), r.disabled = ""
        }, c.onerror = function(e) {
            if ("" == c.currentSrc) return !1;
            alert("Sorry, this image could not be loaded directly*.\nPlease try copy-paste instead.\n\n*probably due to security measures of the browser and/or server. Also, you can't drop local image files from another browser tab.", e)
        };
        var n = new URLSearchParams(window.location.search);
        console.log('n 64', n);
        Array.from(n), window.addEventListener("paste", function(e) {
            var t = (e.clipboardData || e.originalEvent.clipboardData).items;
            console.log(' t68', t);
            for (index in t) {
                var n = t[index];
                console.log('n72', n);
                if ("file" === n.kind) {
                    var a = n.getAsFile(),
                        r = new FileReader;
                    console.log('a 76', a);
                    r.onload = function(e) {
                        console.log('r78', r);
                        console.log('c79', c);
                        c.src = e.target.result
                        console.log('c81', c);
                    }, r.readAsDataURL(a)
                } else "string" === n.kind && n.getAsString(function(e) {
                    b(e) && (c.src = e)
                })
            }
        }), document.getElementById("loadbutton").onclick = function() {

            var n = document.createElement("input");
            console.log('n89', n);
            n.type = "file", n.accept = ".jpg, .jpeg, .png", n.addEventListener("change", function() {
                var e = n.files;
                console.log('e92',e);
                if (0 === e.length);
                else
                    for (var t = 0; t < e.length; t++) f(e[t]) && (c.src = window.URL.createObjectURL(e[t]))
                    console.log('c96 c src', c, '  ', c.src);
            }),
            console.log('n', n);
            console.log("c99 csrc", c, ' ' , c.src);
            console.log("e", e);

            n.click()

        },
         document.body.ondragover = function(e) {
            e.preventDefault()
            console.log(e)
        },
         document.body.ondrop = function(e) {
            if (e.stopPropagation(), e.preventDefault(), e.dataTransfer.items, e.dataTransfer.types, e.dataTransfer.files.length, e.dataTransfer.getData("text"), e.dataTransfer.files.length)
                for (var t, n = e.dataTransfer.files, a = 0; t = n[a]; a++)
                    if ("file" + a + ":" + t.name + t.type || (t.size, t.lastModified), t.type.match("image.*")) {
                        var r = new FileReader;

                        r.onload = function(e) {
                               console.log('r 116', r);
                            c.src = e.target.result;
                            console.log("c 116", c, ' ', c.src);
                            console.log("t", t);

                        }, r.readAsDataURL(t)
                    } else t.type;
            else {
                var o = e.dataTransfer.getData("text");
                console.log('o',o);
                b(o) && (c.src, c.src = o)
                console.log('e',e);
            }
        }, window.addEventListener("keydown", function(e) {
            e.repeat || "Escape" != e.key || (c.src = "", i.width = parseInt(window.getComputedStyle(i.parentNode, null).getPropertyValue("width")), i.height = 150, w(), x())
        });
        var u = !1;

        function w() {
            0 === c.naturalWidth ? v.clearRect(0, 0, v.canvas.width, v.canvas.height) : v.drawImage(c, 0, 0, c.width, c.height, 0, 0, i.width, i.height);
            for (var e = 0; e < y.length; e++) v.strokeStyle = e ? "rgba(0, 255, 0, 1)" : "rgba(255, 0, 0, 1)", v.beginPath(), v.moveTo(y[e].x1, y[e].y1), v.lineTo(y[e].x2, y[e].y2), v.stroke()
        }

        function x() {
            var e = document.getElementById("ref").value.match(/(\d+(,|\.)?\d*)(\D*)/),
                t = "",
                n = "";
            null == e || (t = e[1], n = e[3]);
            var a = parseFloat(t.replace(",", ".")),
                r = 1;
            if (y.length) {
                r = 1 / Math.sqrt(Math.pow(y[0].x1 - y[0].x2, 2) + Math.pow(y[0].y1 - y[0].y2, 2)) * a, m.innerHTML = "";
                for (var o = document.createElement("table"), i = 0; i < y.length; i++) {
                    var d, l = o.insertRow(),
                        s = l.insertCell();
                    s.appendChild(document.createTextNode(i + 1)), r ? d = Math.sqrt(Math.pow(y[i].x1 - y[i].x2, 2) + Math.pow(y[i].y1 - y[i].y2, 2)) * r : (d = Math.sqrt(Math.pow(y[i].x1 - y[i].x2, 2) + Math.pow(y[i].y1 - y[i].y2, 2)), n = " px"), (s = l.insertCell()).appendChild(document.createTextNode(d.toFixed(2) + n)), v.font = "20px serif", v.textAlign = "center", v.textBaseline = "middle";
                    var c = i + 1 + "=" + d.toFixed(2) + n;
                    v.strokeStyle = "rgba(255, 255, 255, 0.5)", v.strokeText(c, Math.min(y[i].x1, y[i].x2) + Math.abs(y[i].x1 - y[i].x2) / 2, Math.min(y[i].y1, y[i].y2) + Math.abs(y[i].y1 - y[i].y2) / 2), v.fillStyle = "rgba(0, 0, 0, 1)", v.fillText(c, Math.min(y[i].x1, y[i].x2) + Math.abs(y[i].x1 - y[i].x2) / 2, Math.min(y[i].y1, y[i].y2) + Math.abs(y[i].y1 - y[i].y2) / 2), s = l.insertCell();
                    var u = document.createElement("a"),
                        p = document.createTextNode("remove");

                    u.appendChild(p), u.href = "", u.onclick = function(e) {
                        return function() {
                            return y.splice(e, 1), w(), x(), !1
                        }
                    }(i), s.appendChild(u)
                }
                var h = o.createTHead().insertRow(),
                    g = document.createTextNode("#"),
                    f = document.createElement("th");

                f.appendChild(g), h.appendChild(f), g = document.createTextNode("length"), (f = document.createElement("th")).appendChild(g), h.appendChild(f), g = document.createTextNode("-"), (f = document.createElement("th")).appendChild(g), h.appendChild(f), m.appendChild(o)
            } else m.innerHTML = ""
        }

        function p(e, t, n) {
            a.textContent = "x=" + e + " y=" + t + " " + n
        }
        window.addEventListener("keydown", function(e) {
            e.repeat || "Control" != e.key || (u = !0)
        }), window.addEventListener("keyup", function(e) {
            e.repeat || "Control" != e.key || (u = !1)
        }), i.addEventListener("mousedown", function(e) {
            return 1 != e.button && d ? (e.stopPropagation(), e.preventDefault(), !1) : 0 == e.button && (e.stopPropagation(), e.preventDefault(), i.oncontextmenu = function() {
                return !1
            }, o = i.getBoundingClientRect(), l = e.clientX - o.left, s = e.clientY - o.top, void(d = !0))
        }), i.addEventListener("mousemove", function(e) {
            o = i.getBoundingClientRect();

            var t = e.clientX - o.left,
                n = e.clientY - o.top,
                a = v.getImageData(t, n, 1, 1).data,
                r = "rgba(" + a[0] + "," + a[1] + "," + a[2] + "," + a[3] + ")";
            p(t.toFixed(), n.toFixed(), r), d && (e.stopPropagation(), e.preventDefault(), w(), y.length ? v.strokeStyle = "rgba(0, 255, 0, 1)" : v.strokeStyle = "rgba(255, 0, 0, 1)", v.beginPath(), v.moveTo(l, s), u && (Math.abs(l - t) <= 10 ? t = l : Math.abs(s - n) <= 10 && (n = s)), v.lineTo(t, n), v.stroke(), v.strokeStyle = "rgba(127, 127, 127, 0.5)", v.beginPath(), v.arc(l + (t - l) / 2, s + (n - s) / 2, Math.sqrt(Math.pow(Math.abs(l - t), 2) + Math.pow(Math.abs(s - n), 2)) / 2, 0, 2 * Math.PI), v.stroke())
        }), i.addEventListener("mouseup", function(e) {
            if (0 != e.button) return !1;
            e.stopPropagation(), e.preventDefault(), i.oncontextmenu = null, d = !1;
            var t = e.clientX - o.left,
                n = e.clientY - o.top;
            l == t && s == n || (u && (Math.abs(l - t) <= 10 ? t = l : Math.abs(s - n) <= 10 && (n = s)), y.push({
                x1: l,
                y1: s,
                x2: t,
                y2: n
            }), x())
        }), i.addEventListener("mouseout", function(e) {

            e.stopPropagation(), e.preventDefault(), p("-", "-", "-")

        }), t.addEventListener("input", function(e) {
            w(), x()
        });
        var h = 0,
            g = "measure_";
        r.value = "Save as '" + g + ("0" + h).slice(-2) + ".png'", r.addEventListener("click", function(e) {
            var t = i.toDataURL("image/png"),
                n = g + ("0" + ++h).slice(-2) + ".png";
            ! function(e, t) {
                var n = document.createElement("a");
                n.href = e, n.setAttribute("download", t);
                var a = document.createEvent("MouseEvents");
                a.initEvent("click", !1, !0), n.dispatchEvent(a)
            }(t, n), r.value = "Save as '" + n + "'"
        })
    })
