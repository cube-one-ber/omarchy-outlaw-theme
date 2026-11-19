return {
  {
    "omacom/aether.nvim",
    branch = "v3",
    name = "aether",
    priority = 1000,
    opts = {
      colors = {
        bg = "#1e1612",
        dark_bg = "#18110e",
        darker_bg = "#110c0a",
        lighter_bg = "#2e211b",

        fg = "#e8dcc4",
        dark_fg = "#a89e98",
        light_fg = "#d8c8ac",
        bright_fg = "#f3f1ef",
        muted = "#906050",

        red = "#e8503a",
        yellow = "#d9a441",
        orange = "#f09c6c",
        green = "#a3a26a",
        cyan = "#86ab9a",
        blue = "#93a6bf",
        magenta = "#c98b8b",
        brown = "#906050",

        bright_red = "#fc603c",
        bright_yellow = "#ffb010",
        bright_green = "#c2c08a",
        bright_cyan = "#a6c8b8",
        bright_blue = "#b2c2d8",
        bright_magenta = "#e2aaa8",

        accent = "#cc6c54",
        cursor = "#f3f1ef",
        foreground = "#e8dcc4",
        background = "#1e1612",
        selection = "#783030",
        selection_foreground = "#f3f1ef",
        selection_background = "#783030",
      },
    },
  },
  {
    "LazyVim/LazyVim",
    opts = {
      colorscheme = "aether",
    },
  },
}
