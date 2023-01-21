-- Function to add tabs before each line within brackets
function tabBrackets(entry)
    local tabbedText = ""
    local tabCount = 0
    local text = entry.data
    for line in string.gmatch(text, "[^\r\n]+") do
        local lowerLine = string.lower(line)
        if tabCount > 1 and (lowerLine:match("%w%w%w%w%s") or lowerLine:match('"####" ') or lowerLine:match('"----" ') or lowerLine:match("'----'") or lowerLine:match("'####'")) and not lowerLine:match("^goto%s") then -- check for 4 letters and whitespace at the beginning of the line, but not "goto"
                tabbedText = tabbedText .. string.rep("\t", tabCount+1) .. line .. "\n"
        elseif string.match(line, "^{%s*$") then -- check for open bracket
            tabbedText = tabbedText .. string.rep("\t", tabCount) .. line .. "\n"
            tabCount = tabCount + 1
        elseif string.match(line, "^}%s*$") then -- check for closed bracket
            tabCount = tabCount - 1
            tabbedText = tabbedText .. string.rep("\t", tabCount) .. line .. "\n"
        else
            tabbedText = tabbedText .. string.rep("\t", tabCount) .. line .. "\n"
        end
    end
    return tabbedText
end

-- Go through all entries in the currently selected archive
local archive = App.currentArchive()
App.logMessage(App.globalError())
for i,entry in ipairs(App.currentEntrySelection()) do
    -- Do search if the entry is opened in the text editor
    if entry.type.editor == 'text' then
        local text = tabBrackets(entry)
        -- give a message box with the output, can't write to another file right now.
        App.messageBoxExt("Here's your output file!", entry.name, text)
    end
end
