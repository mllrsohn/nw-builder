var e=(t=>(t.NIX_32="linux32",t.NIX_64="linux64",t.OSX_32="osx32",t.OSX_64="osx64",t.WIN_32="win32",t.WIN_64="win64",t))(e||{});var m=r=>{switch(r.platform){case"darwin":return r.arch==="x64"?"osx64":"osx32";case"win32":return r.arch==="x64"||r.env.PROCESSOR_ARCHITEW6432?"win64":"win32";case"linux":return r.arch==="x64"?"linux64":"linux32";default:return}},a=m;export{e as Platform,a as detectCurrentPlatform};
