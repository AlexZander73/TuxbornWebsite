(() => {
  const palettes = [
    { name: "Imperial", icon: "IMP", scheme: "default", primary: "amber", accent: "deep-orange" },
    { name: "Stormcloaks", icon: "STO", scheme: "default", primary: "blue", accent: "light-blue" },
    { name: "Thalmor", icon: "THA", scheme: "default", primary: "indigo", accent: "amber" },
    { name: "Dark Brotherhood", icon: "DB", scheme: "slate", primary: "red", accent: "red" },
    { name: "Dawnguard", icon: "DG", scheme: "default", primary: "red", accent: "amber" },
    { name: "Volkihar", icon: "VOL", scheme: "slate", primary: "deep-purple", accent: "red" },
    { name: "Thieves Guild", icon: "TG", scheme: "default", primary: "brown", accent: "orange" },
    { name: "Companions", icon: "CMP", scheme: "default", primary: "green", accent: "lime" },
    { name: "College of Winterhold", icon: "COW", scheme: "default", primary: "cyan", accent: "teal" },
    { name: "Bards College", icon: "BC", scheme: "default", primary: "pink", accent: "deep-orange" },
    { name: "Greybeards", icon: "GB", scheme: "default", primary: "blue-grey", accent: "grey" },
    { name: "Blades", icon: "BLD", scheme: "default", primary: "orange", accent: "deep-orange" },
  ];

  const storageKey = "__palette";

  const getStored = () => {
    try {
      if (typeof window.__md_get === "function") {
        return window.__md_get(storageKey);
      }
      const raw = localStorage.getItem(storageKey);
      return raw ? JSON.parse(raw) : null;
    } catch {
      return null;
    }
  };

  const setStored = (palette) => {
    try {
      if (typeof window.__md_set === "function") {
        window.__md_set(storageKey, palette);
      } else {
        localStorage.setItem(storageKey, JSON.stringify(palette));
      }
    } catch {
      // no-op
    }
  };

  const applyPalette = (palette) => {
    if (!palette) return;
    document.body.setAttribute("data-md-color-scheme", palette.scheme);
    document.body.setAttribute("data-md-color-primary", palette.primary);
    document.body.setAttribute("data-md-color-accent", palette.accent);
    setStored(palette);
  };

  const getCurrentPalette = () => {
    const stored = getStored();
    if (stored) return stored;
    return {
      scheme: document.body.getAttribute("data-md-color-scheme"),
      primary: document.body.getAttribute("data-md-color-primary"),
      accent: document.body.getAttribute("data-md-color-accent"),
    };
  };

  const findPalette = (match) =>
    palettes.find(
      (palette) =>
        palette.scheme === match.scheme &&
        palette.primary === match.primary &&
        palette.accent === match.accent
    );

  const buildSelector = () => {
    const headerInner = document.querySelector(".md-header__inner");
    if (!headerInner || document.getElementById("theme-selector")) return;

    const wrapper = document.createElement("div");
    wrapper.className = "md-theme-selector";

    const trigger = document.createElement("button");
    trigger.type = "button";
    trigger.id = "theme-selector";
    trigger.className = "md-theme-selector__trigger";
    trigger.setAttribute("aria-haspopup", "listbox");
    trigger.setAttribute("aria-expanded", "false");

    const icon = document.createElement("span");
    icon.className = "md-theme-selector__icon";

    const label = document.createElement("span");
    label.className = "md-theme-selector__label";

    const chevron = document.createElement("span");
    chevron.className = "md-theme-selector__chevron";
    chevron.textContent = "▾";

    trigger.appendChild(icon);
    trigger.appendChild(label);
    trigger.appendChild(chevron);

    const menu = document.createElement("div");
    menu.className = "md-theme-selector__menu";
    menu.setAttribute("role", "listbox");
    menu.hidden = true;

    const setDisplay = (palette) => {
      icon.textContent = palette.icon;
      icon.setAttribute("data-faction", palette.name.toLowerCase().replace(/\s+/g, "-"));
      label.textContent = palette.name;
    };

    palettes.forEach((palette) => {
      const option = document.createElement("button");
      option.type = "button";
      option.className = "md-theme-selector__option";
      option.setAttribute("role", "option");
      option.setAttribute("data-theme", palette.name);

      const optIcon = document.createElement("span");
      optIcon.className = "md-theme-selector__icon";
      optIcon.textContent = palette.icon;
      optIcon.setAttribute("data-faction", palette.name.toLowerCase().replace(/\s+/g, "-"));

      const optLabel = document.createElement("span");
      optLabel.textContent = palette.name;

      option.appendChild(optIcon);
      option.appendChild(optLabel);
      option.addEventListener("click", () => {
        applyPalette(palette);
        setDisplay(palette);
        menu.hidden = true;
        trigger.setAttribute("aria-expanded", "false");
        document.documentElement.dispatchEvent(new Event("theme-change"));
      });

      menu.appendChild(option);
    });

    const current = getCurrentPalette();
    const match = findPalette(current) || palettes[0];
    setDisplay(match);

    trigger.addEventListener("click", (event) => {
      event.stopPropagation();
      const next = menu.hidden;
      menu.hidden = !next;
      trigger.setAttribute("aria-expanded", String(next));
    });

    document.addEventListener("click", () => {
      if (!menu.hidden) {
        menu.hidden = true;
        trigger.setAttribute("aria-expanded", "false");
      }
    });

    wrapper.appendChild(trigger);
    wrapper.appendChild(menu);
    headerInner.appendChild(wrapper);
  };

  const init = () => {
    buildSelector();
    const observer = new MutationObserver(() => buildSelector());
    observer.observe(document.body, { childList: true, subtree: true });
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
