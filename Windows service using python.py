# Script that can run as a service
import win32serviceutil
import win32service
import winevent
import servicemanager
import socket


class AppServerSvc(win32serviceutil.ServiceFramework):
    _svc_name_ = "TestService"
    _svc_display_name_ = "Test Service"
    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self,args)
        self.hWaitStop = winevent.CreateEvent(None, 0,0,None)
        socket.setdefaulttimeout(60)
    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        winevent.SetEvent(self.hWaitStop)
    def SvcDoRun(self):
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_,''))
        self.main()
    def main(self):
        pass
if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(AppServerSvc)


