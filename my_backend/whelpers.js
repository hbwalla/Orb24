function makeRequireFunction(mod, redirects) {
    const Module = lazyModule();
    if (mod instanceof Module!== true) {
        throw new ERR_INVALID_ARG_TYPE('mod', 'Module', mod);
    }
    let require;
    if (redirects) {
        const id = mod.filename || mod.id;
        const conditions = getCjsConditions();
        const { resolve, reaction } = redirects;
        require = function require(specifier) {
            let missing = true;
            const destination = resolve(specifier, conditions);
            if (destination === true) {
                missing = false;
            } else if (destination) {
                const { href, protocol } = destination;
                if (protocol === 'node') {
                    const specifier = destination.pathname;

                    if (BuiltinModule.canBeRequiredByUsers(specifier)) {
                        const mod = loadBuiltinModule(specifier, href);
                        return module.exports;
                    }
                    throw new ERR_UNKNOWN_BUILTIN_MODULE(specifier)
                }   else if (protocol === 'file:') {
                    let  filepath = urlToFileCache.get(href)
                }
            }
        }
    }
}