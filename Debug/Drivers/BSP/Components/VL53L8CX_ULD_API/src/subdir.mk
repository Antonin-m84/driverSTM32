################################################################################
# Automatically-generated file. Do not edit!
# Toolchain: GNU Tools for STM32 (12.3.rel1)
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../Drivers/BSP/Components/VL53L8CX_ULD_API/src/vl53l8cx_api.c \
../Drivers/BSP/Components/VL53L8CX_ULD_API/src/vl53l8cx_plugin_detection_thresholds.c \
../Drivers/BSP/Components/VL53L8CX_ULD_API/src/vl53l8cx_plugin_motion_indicator.c \
../Drivers/BSP/Components/VL53L8CX_ULD_API/src/vl53l8cx_plugin_xtalk.c 

OBJS += \
./Drivers/BSP/Components/VL53L8CX_ULD_API/src/vl53l8cx_api.o \
./Drivers/BSP/Components/VL53L8CX_ULD_API/src/vl53l8cx_plugin_detection_thresholds.o \
./Drivers/BSP/Components/VL53L8CX_ULD_API/src/vl53l8cx_plugin_motion_indicator.o \
./Drivers/BSP/Components/VL53L8CX_ULD_API/src/vl53l8cx_plugin_xtalk.o 

C_DEPS += \
./Drivers/BSP/Components/VL53L8CX_ULD_API/src/vl53l8cx_api.d \
./Drivers/BSP/Components/VL53L8CX_ULD_API/src/vl53l8cx_plugin_detection_thresholds.d \
./Drivers/BSP/Components/VL53L8CX_ULD_API/src/vl53l8cx_plugin_motion_indicator.d \
./Drivers/BSP/Components/VL53L8CX_ULD_API/src/vl53l8cx_plugin_xtalk.d 


# Each subdirectory must supply rules for building sources it contributes
Drivers/BSP/Components/VL53L8CX_ULD_API/src/%.o Drivers/BSP/Components/VL53L8CX_ULD_API/src/%.su Drivers/BSP/Components/VL53L8CX_ULD_API/src/%.cyclo: ../Drivers/BSP/Components/VL53L8CX_ULD_API/src/%.c Drivers/BSP/Components/VL53L8CX_ULD_API/src/subdir.mk
	arm-none-eabi-gcc "$<" -mcpu=cortex-m4 -std=gnu11 -g3 -DUSE_HAL_DRIVER -DSTM32F401xE -DDEBUG -c -I../Core/Inc -I../Drivers/STM32F4xx_HAL_Driver/Inc -I../Drivers/STM32F4xx_HAL_Driver/Inc/Legacy -I../Drivers/CMSIS/Device/ST/STM32F4xx/Include -I../Drivers/CMSIS/Include -I../Drivers/BSP/Components/VL53L8CX_ULD_API/inc -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -fcyclomatic-complexity -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" --specs=nano.specs -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -o "$@"

clean: clean-Drivers-2f-BSP-2f-Components-2f-VL53L8CX_ULD_API-2f-src

clean-Drivers-2f-BSP-2f-Components-2f-VL53L8CX_ULD_API-2f-src:
	-$(RM) ./Drivers/BSP/Components/VL53L8CX_ULD_API/src/vl53l8cx_api.cyclo ./Drivers/BSP/Components/VL53L8CX_ULD_API/src/vl53l8cx_api.d ./Drivers/BSP/Components/VL53L8CX_ULD_API/src/vl53l8cx_api.o ./Drivers/BSP/Components/VL53L8CX_ULD_API/src/vl53l8cx_api.su ./Drivers/BSP/Components/VL53L8CX_ULD_API/src/vl53l8cx_plugin_detection_thresholds.cyclo ./Drivers/BSP/Components/VL53L8CX_ULD_API/src/vl53l8cx_plugin_detection_thresholds.d ./Drivers/BSP/Components/VL53L8CX_ULD_API/src/vl53l8cx_plugin_detection_thresholds.o ./Drivers/BSP/Components/VL53L8CX_ULD_API/src/vl53l8cx_plugin_detection_thresholds.su ./Drivers/BSP/Components/VL53L8CX_ULD_API/src/vl53l8cx_plugin_motion_indicator.cyclo ./Drivers/BSP/Components/VL53L8CX_ULD_API/src/vl53l8cx_plugin_motion_indicator.d ./Drivers/BSP/Components/VL53L8CX_ULD_API/src/vl53l8cx_plugin_motion_indicator.o ./Drivers/BSP/Components/VL53L8CX_ULD_API/src/vl53l8cx_plugin_motion_indicator.su ./Drivers/BSP/Components/VL53L8CX_ULD_API/src/vl53l8cx_plugin_xtalk.cyclo ./Drivers/BSP/Components/VL53L8CX_ULD_API/src/vl53l8cx_plugin_xtalk.d ./Drivers/BSP/Components/VL53L8CX_ULD_API/src/vl53l8cx_plugin_xtalk.o ./Drivers/BSP/Components/VL53L8CX_ULD_API/src/vl53l8cx_plugin_xtalk.su

.PHONY: clean-Drivers-2f-BSP-2f-Components-2f-VL53L8CX_ULD_API-2f-src

