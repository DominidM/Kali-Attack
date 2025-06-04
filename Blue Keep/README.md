# Prueba de concepto de Bluekeep

Este repositorio contiene información sobre CVE-2019-0708.

Bluekeep, o CVE-2019-0708, es un exploit de ejecución remota de código (RCE) que afecta a las siguientes versiones de sistemas Windows:

   - Windows 2003
   - Windows XP
   - Windows Vista
   - Windows 7
   - Windows Server 2008
   - Windows Server 2008 R2

La vulnerabilidad se produce durante la preautorización y tiene el potencial de ejecutar código malicioso arbitrario en el contexto de seguridad del usuario de NT Authority\system.

# Cómo funciona

Al enviar un paquete especialmente diseñado, un atacante puede establecer el valor del ID de canal en un valor inesperado para el servicio RDP. Esto provoca un error de corrupción de memoria que crea las condiciones para la ejecución remota de código (RCE). Si el atacante decide continuar con paquetes diseñados para aprovechar esta vulnerabilidad, la ejecución remota de código puede lograrse con privilegios de usuario del sistema.


**Note**

No hay cargas útiles. Esto es solo una PoC. _SIN EMBARGO_ esto se puede portar fácilmente a un exploit ya que puedes agregarle fácilmente cargas útiles.