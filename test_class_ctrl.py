#/*******************************************************************************
#* Copyright 2022 Daniel M. Lofaro
#*
#* Licensed under the Apache License, Version 2.0 (the "License");
#* you may not use this file except in compliance with the License.
#* You may obtain a copy of the License at
#*
#*     http://www.apache.org/licenses/LICENSE-2.0
#*
#* Unless required by applicable law or agreed to in writing, software
#* distributed under the License is distributed on an "AS IS" BASIS,
#* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#* See the License for the specific language governing permissions and
#* limitations under the License.
#*******************************************************************************/
#
#/* Author: Daniel M. Lofaro */

from time import sleep
import darwin_ach as da

def main(args=None):
    # Make Darwin Ach Ros Object
    dar = da.DarwinAchRos(state=True)

    while True:
      des = 0.0
      mes = dar.imu_gyro_y
      e   = des - mes
      k = 10.
      c = k*e
      mot = (1,2)
      if c > 0.6:
        c = 0.6
      if c < -0.6:
        c = -0.6
      pos = (c,-c)
      vel = (100.0, 100.0)

      dar.setMot(mot, pos, vel)
      print(e)
      sleep(0.01)

    # Kill Node
    dar.close()


if __name__ == '__main__':
    main()

