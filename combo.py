a
    ��`�  �                	   @   s(  d dl Z d dlZd dlZd dlZd Zdd� ZdZdZdZ	dZ
dZdZd	Zd
ZdZdZdZedjee	e
eeed�� ed� d Zed�Zeed��Zee�D ]FZed7 Zed�dd� ed�D ���Zede d e � e�d� q�edd��&Z e �!ed e d � W d  � n1 �s0    Y  dS )�    Nc                 C   s2   | d D ]$}t j�|� t j��  t�d� qd S )N�
gE'��q?)�n�stdout�write�flush�mm�sleep)�M�c� r   �/sdcard/Download/tr.py�slow   s    
r   Z
1280973645Z?qwertyuiopasdfghjklzxcvbnm_QWERTYUIOPASDFGHJKLZXCVBNM1234567890z[1;32mz[1;31mz[1;36m�l�B�Dz[1;37mz@
{e}
{p}{i}AUTHER{p}:{h}XOSHNAW {B}
{p}{i}TELEGRAM{p}:{h}@Y_0_U
)�i�h�p�e�gr   aG  [1;32m~[1;32m~[1;32m~[1;32m~[1;32m~[1;32m~[1;32m~[1;32m~[1;32m~[1;32m~[1;32m~[1;32m~[1;32m~[1;32m~[1;32m~[1;32m~[1;32m~[1;32m~[1;32m~[1;32m~[1;32m~[1;32m~[1;32m~[1;32m~[1;32m~[1;32m~[1;32m~[1;32m~[1;32m~[1;32m~[1;32m~[1;32m~[1;32m~[1;32m~[1;32m~[1;32m~[1;32m~[1;32m~[1;32m~[1;32m~[1;37mz[1;37m(EMAIL) YAN (RAQAM) : z[1;37mCHAND DANAT AWE: �   � c                 c   s   | ]}t �t�V  qd S )N)�randomZchoice�number)�.0r   r   r   r   �	<genexpr>%   �    r   �   z[1;33m�:g-C��6?zNum.txt�az|@Y_0_U
)"r   �time�sysr   r   �countr   Zcombor   ZgreenZpadZredZmusZrfZkfZmustZrg�hi�formatr   �inputZXoshnaw�int�w�ranger   �str�joinZpas�printr   �open�xr   r   r   r   r   �<module>   s<   �