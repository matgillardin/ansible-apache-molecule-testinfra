import os
import testinfra.utils.ansible_runner

# Récupération de l'inventaire Molecule
testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_apache_package_installed(host):
    """
    Vérifie que le paquet Apache2 est installé
    """
    apache = host.package("apache2")
    assert apache.is_installed


def test_apache_service_running(host):
    """
    Vérifie que le service Apache2 est démarré
    """
    apache_service = host.service("apache2")
    assert apache_service.is_running


def test_apache_service_enabled(host):
    """
    Vérifie que le service Apache2 est activé au démarrage
    """
    apache_service = host.service("apache2")
    assert apache_service.is_enabled


def test_custom_config_file_exists(host):
    """
    Vérifie que le fichier de configuration personnalisé existe
    """
    config_file = host.file("/etc/apache2/sites-available/custom-site.conf")
    assert config_file.exists


def test_custom_config_file_permissions(host):
    """
    Vérifie les permissions du fichier de configuration
    """
    config_file = host.file("/etc/apache2/sites-available/custom-site.conf")
    assert config_file.user == "root"
    assert config_file.group == "root"
    assert config_file.mode == 0o644


def test_custom_config_file_content(host):
    """
    Vérifie que le fichier de configuration contient les bonnes directives
    """
    config_file = host.file("/etc/apache2/sites-available/custom-site.conf")
    assert config_file.contains("ServerAdmin webmaster@localhost")
    assert config_file.contains("DocumentRoot /var/www/html")


def test_apache_listening_port_80(host):
    """
    Vérifie qu'Apache écoute sur le port 80
    """
    socket = host.socket("tcp://0.0.0.0:80")
    assert socket.is_listening
