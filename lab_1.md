# Lab 1 — Cyber Threat Intelligence (CTI) Report Mapping to MITRE ATT&CK

## Group Members
- Nadav Shapira (ID: 325363505)

## Source CTI Report
**Title:** SUNBURST Backdoor – SolarWinds Supply Chain Compromise  
**Source:** Microsoft Security Blog  
**Link:** https://www.microsoft.com/security/blog/2020/12/13/analyzing-solorigate-the-compromised-dll-file-that-started-a-sophisticated-cyberattack/

## Short Attack Summary
The SolarWinds SUNBURST attack was a large-scale supply chain compromise in which attackers inserted a malicious backdoor into a legitimate SolarWinds Orion software update. When customers installed the trojanized update, the malware quietly established persistence and communicated with attacker-controlled command-and-control (C2) servers. The attackers selectively activated follow-on actions only for high-value targets, reducing the chance of detection. The campaign affected government agencies and major enterprises, demonstrating the strategic impact of supply chain attacks. This incident matters because it showed how trusted software updates can be abused to bypass traditional security controls. It also highlighted the importance of behavioral detection and threat intelligence sharing.

## Attack Diagram / Sequence
```
[Attacker]
    |
    v
[Compromise SolarWinds Build Environment]
    |
    v
[Malicious DLL Signed & Distributed]
    |
    v
[Victim Installs Orion Update]
    |
    v
[SUNBURST Dormant Period]
    |
    v
[DNS-based C2 Communication]
    |
    v
[Selective Lateral Movement & Data Exfiltration]
```

## MITRE ATT&CK Mapping

| Tactic | Technique | Behavior from the Report | ATT&CK Link |
|-------|-----------|--------------------------|-------------|
| Initial Access | Supply Chain Compromise | Malicious code inserted into SolarWinds Orion updates | https://attack.mitre.org/techniques/T1195/ |
| Execution | Command and Scripting Interpreter | SUNBURST executed as a trusted SolarWinds service | https://attack.mitre.org/techniques/T1059/ |
| Persistence | Boot or Logon Autostart Execution | Malicious DLL loaded on service start | https://attack.mitre.org/techniques/T1547/ |
| Defense Evasion | Signed Binary Proxy Execution | Abuse of digitally signed SolarWinds binaries | https://attack.mitre.org/techniques/T1218/ |
| Command and Control | DNS | C2 communication over DNS to attacker domains | https://attack.mitre.org/techniques/T1071/004/ |
| Lateral Movement | Remote Services | Use of compromised credentials to move within networks | https://attack.mitre.org/techniques/T1021/ |
| Exfiltration | Exfiltration Over C2 Channel | Sensitive data exfiltrated via existing C2 | https://attack.mitre.org/techniques/T1041/ |

## Insights / What We Learned
This case demonstrates how advanced attackers map multiple ATT&CK techniques into a long-term, stealthy campaign. Supply chain compromise provides powerful initial access while minimizing noise. Mapping CTI reports to MITRE ATT&CK helps defenders understand attacker behavior patterns and improve detection across the full attack lifecycle.

