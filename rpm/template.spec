Name:           ros-hydro-iiwa
Version:        2.0.2
Release:        0%{?dist}
Summary:        ROS iiwa package

Group:          Development/Libraries
License:        BSD
URL:            http://lasa.epfl.ch/khansari
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-message-runtime
Requires:       ros-hydro-sensor-msgs
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-message-generation
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-sensor-msgs

%description
IIWA Robot

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Tue Apr 14 2015 Mohammad Khansari <khansari@cs.stanford.edu> - 2.0.2-0
- Autogenerated by Bloom

* Thu Apr 09 2015 Mohammad Khansari <khansari@cs.stanford.edu> - 2.0.1-0
- Autogenerated by Bloom

* Tue Apr 07 2015 Mohammad Khansari <khansari@cs.stanford.edu> - 2.0.0-2
- Autogenerated by Bloom

* Mon Mar 30 2015 Mohammad Khansari <khansari@cs.stanford.edu> - 2.0.0-1
- Autogenerated by Bloom

* Mon Mar 30 2015 Mohammad Khansari <khansari@cs.stanford.edu> - 2.0.0-0
- Autogenerated by Bloom

