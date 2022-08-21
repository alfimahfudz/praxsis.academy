<#
.SYNOPSIS
   Shows when last PC started up.
.DESCRIPTION
   This is a WMI wrapper function to get the time that your PC last started up.
.PARAMETER ComputerName
    The name of the computer you want to run the command againts.
.EXAMPLE
    Get-LastBootTime -ComputerName localhost
.LINK
    www.howtogeek.com
#>    
param(
    [Parameter(Mandatory=$true)][string]$ComputerName
)

Get-WmiObject -Class Win32_OperatingSystem -ComputerName $ComputerName |
Select-Object -Property CSName,@{n="LastBootUpTime";
e={[Management.ManagementDateTimeConverter]::ToDateTime($_.LastBootUpTime)}}
