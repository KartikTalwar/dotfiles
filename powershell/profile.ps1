# C:\Users\Kartik\Documents\web\github\dotfiles\powershell\profile.ps1

$a = (Get-Host).UI.RawUI
$a.WindowTitle = "Fake Shell"

Push-Location (Split-Path -Path $MyInvocation.MyCommand.Definition -Parent)

# Load posh-git module from current directory
Import-Module "C:\Users\Kartik\Documents\WindowsPowerShell\Modules\posh-git"

# If module is installed in a default location ($env:PSModulePath),
# use this instead (see about_Modules for more information):
# Import-Module posh-git

# Set up a simple prompt, adding the git prompt parts inside git repos
function prompt {
    $realLASTEXITCODE = $LASTEXITCODE

    # Reset color, which can be messed up by Enable-GitColors
    $Host.UI.RawUI.ForegroundColor = $GitPromptSettings.DefaultForegroundColor

    Write-Host($pwd) -nonewline

    Write-VcsStatus

    $global:LASTEXITCODE = $realLASTEXITCODE
    return "> "
}

Enable-GitColors

Pop-Location

Start-SshAgent -Quiet
