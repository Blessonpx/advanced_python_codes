# script.ps1

# Check if any arguments have been passed
if ($args.Count -gt 0) {
    Write-Host "Argument received"
    Write-Host $args[0]
    git add .
    git commit -am $args[0]
    git push -u origin main
} else {
    Write-Host "No Arguments"
    $x=Get-Date -Format "dd-MM-yy HH:mm:ss"
    Write-Host $x
    git add .
    git commit -am $x
    git push -u origin main
}
