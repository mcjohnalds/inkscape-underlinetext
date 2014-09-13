# Underline Text for Inkscape

The newer versions of inkscape (>=.9) support displaying underlined text, but
lack any buttons or key bindings. This extension adds a menu option under
`Extensions/Text/Underline Text` and a keybinding (Shift-u) that underlines
selected text objects.

## Installation

### If you haven't changed inkscape's keybindings

```bash
git clone https://github.com/mcjohnalds/inkscape-underlinetext.git
mv inkscape-underlinetext/* ~/.config/inkscape
rm -rf inkscape-underlinetext
```

### If you have changed inkscape's keybindings

```bash
git clone https://github.com/mcjohnalds/inkscape-underlinetext.git
mv inkscape-underlinetext/extensions ~/.config/inkscape
rm -rf inkscape-underlinetext

Then manually add the following lines to your
`~/.config/inkscape/keys/default.xml`:

```xml
<bind key="u" modifiers="Shift" action="mcjohnalds.underlinetext" display="true"/>
<bind key="U" modifiers="Shift" action="mcjohnalds.underlinetext"/>
```

# Uninstallation

### If you haven't changed inkscape's keybindings

```bash
rm ~/.config/inkscape/extensions/underlinetext.* ~/.config/inkscape/keys/default.xml
```

### If you have changed inkscape's keybindings

```bash
rm ~/.config/inkscape/extensions/underlinetext.*
```

Then manually delete the following lines from you
`~/.config/inkscape/keys/default.xml`:

```xml
<bind key="u" modifiers="Shift" action="mcjohnalds.underlinetext" display="true"/>
<bind key="U" modifiers="Shift" action="mcjohnalds.underlinetext"/>
```