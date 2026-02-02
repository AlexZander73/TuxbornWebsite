(() => {
  const buildTable = (container, data) => {
    container.innerHTML = "";

    const table = document.createElement("table");
    table.className = "md-typeset checklist-table__table";

    const thead = document.createElement("thead");
    const headerRow = document.createElement("tr");
    data.headers.forEach((header) => {
      const th = document.createElement("th");
      th.textContent = header;
      headerRow.appendChild(th);
    });
    thead.appendChild(headerRow);
    table.appendChild(thead);

    const tbody = document.createElement("tbody");
    data.rows.forEach((row) => {
      const tr = document.createElement("tr");
      row.forEach((cell) => {
        const td = document.createElement("td");
        td.textContent = cell;
        tr.appendChild(td);
      });
      tbody.appendChild(tr);
    });
    table.appendChild(tbody);

    container.appendChild(table);
  };

  const initTables = () => {
    document.querySelectorAll(".checklist-table").forEach((container) => {
      const raw = container.getAttribute("data-checklist");
      if (!raw) return;
      const data = JSON.parse(raw);
      buildTable(container, data);

      const wrapper = container.closest(".md-typeset") || document;
      const searchInput = wrapper.querySelector(".checklist-search");
      const filtersWrapper = wrapper.querySelector(".checklist-filters");
      const table = container.querySelector("table");
      if (!table) return;

      const rows = Array.from(table.querySelectorAll("tbody tr"));
      const headers = Array.from(table.querySelectorAll("thead th")).map((th) => th.textContent);

      const columnFilters = headers
        .map((header, index) => ({ header, index }))
        .filter(({ header }) => header && header.toLowerCase() !== "tab");

      const filterControls = [];
      columnFilters.forEach(({ header, index }) => {
        const values = new Set();
        rows.forEach((row) => {
          const cell = row.children[index];
          if (cell && cell.textContent.trim()) values.add(cell.textContent.trim());
        });
        if (values.size === 0 || values.size > 30) return;

        const select = document.createElement("select");
        select.setAttribute("data-filter-index", String(index));
        const defaultOption = document.createElement("option");
        defaultOption.value = "";
        defaultOption.textContent = `${header}: All`;
        select.appendChild(defaultOption);

        Array.from(values)
          .sort((a, b) => a.localeCompare(b))
          .forEach((value) => {
            const option = document.createElement("option");
            option.value = value;
            option.textContent = value;
            select.appendChild(option);
          });

        filtersWrapper?.appendChild(select);
        filterControls.push(select);
      });

      const applyFilters = () => {
        const query = searchInput?.value.trim().toLowerCase() || "";
        const selections = filterControls.map((select) => ({
          index: Number(select.getAttribute("data-filter-index")),
          value: select.value,
        }));

        rows.forEach((row) => {
          const text = row.textContent.toLowerCase();
          const matchesQuery = !query || text.includes(query);
          const matchesFilters = selections.every(({ index, value }) => {
            if (!value) return true;
            const cell = row.children[index];
            return cell && cell.textContent.trim() === value;
          });
          row.style.display = matchesQuery && matchesFilters ? "" : "none";
        });
      };

      if (searchInput) {
        searchInput.addEventListener("input", applyFilters);
      }
      filterControls.forEach((select) => select.addEventListener("change", applyFilters));
    });
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initTables);
  } else {
    initTables();
  }
})();
