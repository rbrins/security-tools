Import-Module ExchangeOnlineManagement

$startDate = Get-Date "01/01/1970"
$endDate = Get-Date "01/01/1971"


<# The account that you use to connect must be enabled for remote PowerShell. For more information, see Enable or disable access to Exchange Online PowerShell. https://learn.microsoft.com/en-us/powershell/exchange/disable-access-to-exchange-online-powershell?view=exchange-ps #>
$UserPN = ""

<# not using -UseRPSSession because it looks like it might use local session, not using -PSSessionOption with ProxyOption because no proxy #>
<# might need - managed identity information depending on okta config - https://learn.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/overview #>
<# might need - $UserCredential = Get-Credential \n Connect-IPPSSession -Credential $UserCredential #>
Write-Output "[ ] Connecting with $UserPN"
Connect-IPPSSession -UserPrincipalName $UserPN
Write-Output "[+] Connected with $UserPN"

<# Do the things here - note this is not complete #>
<# probably from - https://learn.microsoft.com/en-us/powershell/module/exchange/?source=recommendations&view=exchange-ps #>

<# This example returns a summary list of the rules for EOP protections in preset security policies. #>
<# Get-EOPProtectionPolicyRule | Format-Table Name,State #> 

<# this should list all of the qurantinedmessages with a date #>
Write-Output "[ ] Getting Quaratine Messages during specified time"
Get-QuarantineMessage -StartReceivedDate $startDate -EndReceivedDate $endDate 
$countMessages = Get-QuarantineMessage -StartReceivedDate $startDate -EndReceivedDate $endDate | Measure-Object 
Write-Output "$countMessages"
<# should format and transform here #>

<# for counting by types can use -PolicyTypes  #>
<# with AntiMalwarePolicy AntiPhishPolicy ExchangeTransportRule HostedContentFilterPolicy or SafeAttachmentPolicy as the options #>
<# for quarantine types can use -QuarantineTypes #>
<# with Bulk HighConfPhish Malware Phish Spam SPOMalware TransportRule #>
<# -RecipientAddress can be one #>


<# Disconnect when finished with confirmation prompt (can disable with -Confirm:$false) #>
Disconnect-ExchangeOnline -Confirm:$false

