<?php

interface iCache {
	/**
	 * 	Interface to be followed by all cache classes
	 */
	public function add(key, value);
	public function set(key, value);
	public function get(key, value);
	public function delete(key, value);
}

interface iCacheObj {
	public function getKey();
	public function getValue();
}

abstract class cacheObj implements iCacheObj {
	private $_key;
	private $_value;

	private function __construct($key, $value) {
		$this->_key = $key;
		$this->_value = $value;
	}

	public function getKey() {
		return $this->_key;
	}

	public function getValue() {
		return $this->_value;
	}
}

class LRUCacheObj extends cacheObj {
	// Nothing to do here really, all the functionality we need is already there.
}

class LRUCache implements iCache {
	
}