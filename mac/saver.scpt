tell application "iTerm"
    activate
    tell application "System Events"
        keystroke "t" using {command down}
        keystroke "python ~/repos/fake-terminal-screensaver/saver.py"
        keystroke return
    end tell
end tell
